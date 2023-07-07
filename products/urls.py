from django.urls import path
from .views import CategoryView, ProductView, VariantView, PriceView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryView.as_view(), name='category-detail'),
    path('products/', ProductView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product-detail'),
    path('variants/', VariantView.as_view(), name='variant-list'),
    path('variants/<int:variant_id>/', VariantView.as_view(), name='variant-detail'),
    path('prices/', PriceView.as_view(), name='price-list'),
    path('prices/<int:price_id>/', PriceView.as_view(), name='price-detail'),
]
