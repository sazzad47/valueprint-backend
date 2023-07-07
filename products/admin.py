from django.contrib import admin
from .models import Category, Product, Variant, Price

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Price)
