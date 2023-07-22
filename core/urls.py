from django.urls import path
from .views import OrderCreateView, OrderUpdateView, OrderDetailView, OrderListView, PaymentIntentCreateView, stripe_webhook, UserTransactionsView, OrderAllListView, send_contact_form_email

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/all/', OrderAllListView.as_view(), name='order-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/edit/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('create-payment/', PaymentIntentCreateView.as_view(), name='create-payment'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('transactions/', UserTransactionsView, name='user_transactions'),
    path('send-contact-form-email/', send_contact_form_email, name='send_contact_form_email'),

]
