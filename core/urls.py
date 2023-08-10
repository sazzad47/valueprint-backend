from django.urls import path
from .views import OrderCreateView, OrderUpdateView, OrderDetailView, OrderListView, PaymentIntentCreateView, stripe_webhook, UserTransactionsView, OrderAllListView, send_contact_form_email, UserAllTransactionsView, DeleteTransactionView, UserAllOrdersView, UpdateOrderStageView, UserGetOrdersByStageView, send_quotation_request_email

urlpatterns = [
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/all/', OrderAllListView.as_view(), name='order-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/edit/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('create-payment/', PaymentIntentCreateView.as_view(), name='create-payment'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('transactions/', UserTransactionsView, name='user_transactions'),
    path('transactions/all/', UserAllTransactionsView, name='user_all_transactions'),
    path('transactions/<int:transaction_id>/delete/', DeleteTransactionView, name='transactions_delete'),
    path('orders/admin/all/', UserAllOrdersView, name='admin_all_orders'),
    path('orders/admin/update/<int:order_id>/', UpdateOrderStageView, name='admin_all_orders'),
    path('orders/<str:stage>/', UserGetOrdersByStageView.as_view(), name='admin_all_orders'),
    path('send-contact-form-email/', send_contact_form_email, name='send_contact_form_email'),
    path('send-quote-req-email/', send_quotation_request_email, name='send_quotation_request_email'),

]
