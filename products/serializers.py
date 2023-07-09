from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'category_name', 'name', 'photo', 'options', 'cover', 'information', 'artwork', 'templates', 'faq', 'features', 'variants', 'rp', 'dp', 'price']

    def get_category_name(self, product):
        return product.category.name if product.category else None

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, category):
        return category.product_set.count()

