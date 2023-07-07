from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Variant, Price
from .serializers import CategorySerializer, ProductSerializer, VariantSerializer, PriceSerializer

class CategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VariantView(APIView):
    def post(self, request):
        serializer = VariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, variant_id):
        variant = Variant.objects.get(pk=variant_id)
        serializer = VariantSerializer(variant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, variant_id):
        variant = Variant.objects.get(pk=variant_id)
        variant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PriceView(APIView):
    def post(self, request):
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, price_id):
        price = Price.objects.get(pk=price_id)
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, price_id):
        price = Price.objects.get(pk=price_id)
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
