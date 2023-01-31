""" App Profile
"""
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from django.contrib.auth.models import User


class CreateUser(ListView):
    model = User
    template_name = 'user_profile/index_profile.html'
    context_object_name = 'Users'


class UpdateUser(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass
