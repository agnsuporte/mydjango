"""store URL Configuration

"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateUser.as_view(), name='create_user'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
