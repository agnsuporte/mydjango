"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product'),
    path('<slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('car/', views.ProductCar.as_view(), name='product_car'),
    path('addcar/', views.ProductAddCar.as_view(), name='product_add_car'),
    path('removecar/', views.ProductRemoveCar.as_view(), name='product_remove_car'),
    path('checkout/', views.ProductCheckout.as_view(), name='product_checkout'),
]
