from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveAPIView
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from rest_framework import generics
from django.db.models import Q


class CategoryView(APIView):
    
    def post(self, request):
        # if not request.user.is_staff:
        #     return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)

            return Response({
                "message": "Category updated successfully.",
                "categories": serializer.data
            }, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id):
        # if not request.user.is_staff:
        #     return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)

            return Response({
                "message": "Category updated successfully.",
                "categories": serializer.data
            }, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = Category.objects.order_by('id')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteView(APIView):
    def delete(self, request, category_id):
        if not request.user.is_staff:
            return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        try:
            category = Category.objects.get(pk=category_id)
            category.delete()

             # Get all the remaining categories
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)

            return Response({
                "message": "Category deleted successfully.",
                "categories": serializer.data
            }, status=status.HTTP_200_OK )
        
        except Category.DoesNotExist:
            return Response({"message": "Category not found."}, status=status.HTTP_404_NOT_FOUND)


class ProductView(APIView):
    
    def post(self, request):
        # if not request.user.is_staff:
        #     return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        # if not request.user.is_staff:
        #     return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Product.objects.order_by('id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(APIView):
    def delete(self, request, product_id):
        # if not request.user.is_staff:
        #     return Response({"message": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return Response({"message": "Product deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"message": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Product.objects.filter(Q(category__name__icontains=category_name))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(name__icontains=category_name).first()

        category_serializer = CategorySerializer(category)
        product_serializer = self.get_serializer(queryset, many=True)

        return Response({
            'category': category_serializer.data,
            'products': product_serializer.data,
        })
