"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PayOrder.as_view(), name='order'),
    path('detail/<int:pk>', views.OrderDetail.as_view(), name='order_detail'),
    path('close/', views.CloseOrder.as_view(), name='close_order'),
]
