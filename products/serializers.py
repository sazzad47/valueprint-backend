from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'category_name', 'name', 'slogan', 'photo', 'pdf', 'intro_photo', 'cover_photo', 'rating', 'starting_quantity', 'starting_price', 'options', 'cover', 'short_description', 'perfect_for', 'ideas', 'information', 'artwork', 'templates', 'design_services', 'faq', 'intro', 'features', 'variants', 'rp', 'dp', 'price', 'pricing']

    def get_category_name(self, product):
        return product.category.name if product.category else None

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count', 'photo', 'cover', 'information']

    def get_products_count(self, category):
        return category.product_set.count()

