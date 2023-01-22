"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_product, name='index_product'),
    # path('contact/', include('contact.urls')),
]
