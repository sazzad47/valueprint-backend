from rest_framework import serializers
from .models import Category, Product, Variant, Price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'variant', 'quantity', 'price']

class VariantSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)

    class Meta:
        model = Variant
        fields = ['id', 'product', 'name', 'prices']

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'variants']
