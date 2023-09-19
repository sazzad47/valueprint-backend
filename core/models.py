from django.db import models
from django.conf import settings
from django.utils.html import format_html

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Processing', 'Processing'),
        ('Submitted', 'Submitted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='it_orders')
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    shipping_address = models.JSONField(blank=True, null=True)
    order_details = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, default='unpaid', blank=True)
    stage = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', blank=True)

    def __str__(self):
        return f"Order #{self.pk} - User: {self.user.email}"


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='it_transactions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Transaction #{self.pk} - User: {self.user.email}"
    
class Blog(models.Model):

    title = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.URLField(blank=False, null=False)
    cover_photo = models.URLField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title


