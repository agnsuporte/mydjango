"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_order, name='index_order'),
    # path('contact/', include('contact.urls')),
]
