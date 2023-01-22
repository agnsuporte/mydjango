"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_profile, name='index_profile'),
    # path('contact/', include('contact.urls')),
]
