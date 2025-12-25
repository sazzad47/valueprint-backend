from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderListSerializer, OrderItemSerializer, TransactionSerializer
from .models import Order, Transaction
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import stripe
from utils import Util
from django.conf import settings
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from utils import Util
from rest_framework.decorators import api_view
from app.settings import BASE_CLIENT_URL
import json
from django.shortcuts import get_object_or_404
import os
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.views import APIView



class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        self.send_order_received_email(order)
    
    def send_order_received_email(self, order):
        subject = "Order Received"
        body = f"Dear {order.user.first_name},\n\nThank you for placing an order with us. Your order with ID #{order.pk} ({order.title}) has been received by our team. We will review your order and provide you with further details soon.\n\nWe appreciate your patience, and if you have any questions, feel free to reach out to us. Thank you for choosing our services!\n\nBest regards,\nSazzad Hossen"
        html_body = f"<p>Dear {order.user.first_name},</p><p>Thank you for placing an order with us. Your order with ID #{order.pk} ({order.title}) has been received by our team. We will review your order and provide you with further details soon.</p><p>We appreciate your patience, and if you have any questions, feel free to reach out to us. Thank you for choosing our services!</p><p>Best regards,<br>Sazzad Hossen</p>"
        to_email = order.user.email
       

        data = {
            'subject': subject,
            'body': body,
            'html_body': html_body,
            'to_email': to_email,
        }

        Util.send_email(data)

class OrderAllListView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)  # Use your custom serializer for the Order model
        return Response(serializer.data)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentIntentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Make sure data is a dictionary
            data = request.data if isinstance(request.data, dict) else {}
            print(request.user.id)
            user = request.user if request.user.is_authenticated else None
            
            # Modify the metadata dictionary to include the user ID
            metadata = data.get('metadata', {})
            cart_items_str = metadata.get('cart_items', '[]')  # Default to an empty list if 'cart_items' key is not present
            order_id = metadata.get('order_id', None)  
            cart_items = json.loads(cart_items_str)
            # Retrieve the line_items from the data dictionary
            line_items = data.get('line_items', [])
            
            if order_id is not None:
                # If order_id is provided, check if the order with the given order_id exists
                order = get_object_or_404(Order, id=order_id)
                # If the order exists, update its order_details and status instead of creating a new one
                order.order_details = cart_items
                order.status = 'unpaid'
                order.save()
            else:
                # If order_id is not provided, create a new order
                order = Order.objects.create(
                    user=user,
                    email=user.email,
                    order_details=cart_items,  
                    status='unpaid',
                    stage='pending'
                )
            
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                shipping_address_collection={
                    'allowed_countries': ['SG'], 
                },
                metadata= {
                    'order_id': order.id
                },
                mode='payment',
                success_url=BASE_CLIENT_URL + '/' + 'payment-success',
                cancel_url=BASE_CLIENT_URL + '/' + 'cart'
            )
            
            return Response({'checkout_url': checkout_session.url})
        except Exception as e:
            return Response({'msg': 'something went wrong while creating stripe session', 'error': str(e)}, status=500)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        metadata = session.get('metadata', {})
        order_id = metadata.get('order_id', None)
        customer_details = session.get('customer_details', {})
        name = customer_details.get('name', '')  
        email = customer_details.get('email', '')
        shipping_details = session.get('shipping_details', {})
        shipping_address = shipping_details.get('address', {})  # Returns 'Jahangirnagar University'
        print(metadata)

        try:
            # Update the order only if the payment is successful
            if session['payment_status'] == 'paid':
                # Update the order
                order = Order.objects.get(pk=order_id)  # Use get instead of find
                order.name = name
                order.email = email
                order.shipping_address = shipping_address
                order.status = 'Paid'
                order.stage = 'Pending'
                order.save()

                # Create a new transaction instance
                Transaction.objects.create(
                    user=order.user,
                    order=order,
                    amount=session['amount_total'] / 100,  # Convert cents to the currency
                    payment_id=session['id'],
                    status='Completed'
                )

                # Sending confirmation email to the customer
                subject = "Payment Received"
                message = f"Dear {name},<br><br>" \
                          f"Your payment for order {order.id} has been received.<br><br>" \
                          f"Order Details:<br><br>"\
                          f"ID: {order.id}<br>"\
                          f"Total Price: S${session['amount_total'] / 100}<br>"\
                          f"Status: {order.status}<br><br>"\
                          f"If you have any questions or need further assistance, please don't hesitate to contact us.<br><br>"\
                          f"Best regards,<br>"\
                          f"Value Print Pte Ltd"
                data = {
                    'subject': subject,
                    'body': '',
                    'html_body': message,
                    'to_email': email
                }
                Util.send_email(data)

        except Exception as e:
            # Handle order creation error
            print("Error occurred while creating order:")
            print(str(e))  # Print the error message and stack trace in the terminal
            return JsonResponse({'error': 'Failed to create order', 'details': str(e)}, status=500)

       
    # Passed signature verification
    return HttpResponse(status=200)

@api_view(['GET'])
def UserTransactionsView(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserAllTransactionsView(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteTransactionView(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        return Response({'message': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        transaction.delete()
        return Response({'message': 'Transaction deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def UserAllOrdersView(request):
    orders = Order.objects.filter(status='Paid')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def UpdateOrderStageView(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        new_stage = request.data.get('stage')
        if new_stage is not None:
            order.stage = new_stage
            order.save()
            return Response({'message': 'Order stage updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid data, stage not provided'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def send_contact_form_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            contact_number = data.get('contactNumber')
            print_category = data.get('printCategory')
            artwork_ready = data.get('artworkReady')
            quantity = data.get('quantity')
            message = data.get('message')

            # Send email using Django's send_mail function
            subject = f"Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\nContact Number: {contact_number}\nPrint Category: {print_category}\nArtwork Ready: {artwork_ready}\nQuantity: {quantity}\nMessage: {message}"
            from_email = email  # Replace with your email address
            to_email = os.environ.get('EMAIL_FROM') # Replace with the recipient's email address
            send_mail(subject, body, from_email, [to_email])

            return JsonResponse({'message': 'Form submitted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
@api_view(['POST'])
def send_quotation_request_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            contact_number = data.get('contact_number')
            print_category = data.get('print_category')
            sheet_type = data.get('sheet_type')
            delivery_date = data.get('delivery_date')
            is_ready_customer = data.get('is_ready_customer')
            budget = data.get('budget')
            artFile = data.get('artFile')

            # Send email using Django's send_mail function
            subject = f"Quotation request from {first_name} {last_name}"
            body = f"Name: {first_name} {last_name}\nEmail: {email}\nContact Number: {contact_number}\nPrint Category: {print_category}\nLoose Sheet?: {sheet_type}\nDelivery Date: {delivery_date}\nBudget: {budget}\nIs Customer Ready?: {is_ready_customer}\nUploaded File: {artFile}"
            from_email = email  # Replace with your email address
            to_email = os.environ.get('EMAIL_FROM') # Replace with the recipient's email address
            send_mail(subject, body, from_email, [to_email])

            return JsonResponse({'message': 'Form submitted successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


class UserGetOrdersByStageView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        stage = self.kwargs['stage']
        if stage is not None:
            return Order.objects.filter(stage__iexact=stage, status='Paid')
        else:
            return Order.objects.filter(status='Paid')

