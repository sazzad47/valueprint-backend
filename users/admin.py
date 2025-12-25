from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, BillingAddress

class UserModelAdmin(BaseUserAdmin):

    list_display = ('id', 'email', 'first_name', 'last_name', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
admin.site.register(BillingAddress)
