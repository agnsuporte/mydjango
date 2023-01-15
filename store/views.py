"""
    store URL Configuration
"""
from django.shortcuts import render, HttpResponse


# Home page
def index_home(request):
    return render(request, 'home.html')
