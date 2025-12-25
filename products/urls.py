from django.urls import path
from .views import (
    CategoryView,
    CategoryDetailView,
    CategoryDeleteView,
    ProductView,
    ProductDetailView,
    ProductDeleteView,
    ProductByCategoryView
)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<int:category_id>/update/', CategoryView.as_view(), name='category-detail-update'),
    path('categories/<int:pk>/get/', CategoryDetailView.as_view(), name='category-detail-get'),
    path('categories/<int:category_id>/delete/', CategoryDeleteView.as_view(), name='category-detail-delete'),
    path('list/', ProductView.as_view(), name='product-list'),
    path('list/<int:product_id>/update/', ProductView.as_view(), name='product-detail-update'),
    path('list/<int:pk>/get/', ProductDetailView.as_view(), name='product-detail-get'),
    path('list/<int:product_id>/delete/', ProductDeleteView.as_view(), name='product-detail-delete'),
    path('list/<str:category_name>/', ProductByCategoryView.as_view(), name='product-by-category'),
]
