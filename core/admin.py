from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.conf import settings
from .models import Order
from utils import Util
from .models import Transaction
from django import forms
from django.contrib.auth.models import Group

class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ('status',)
    list_filter = ('status',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__email', 'order__title')

admin.site.unregister(Group)