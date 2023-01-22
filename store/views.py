"""
    store URL Configuration
"""
from django.shortcuts import render


def index_home(request: any) -> render:
    """Return the /templates/home.html."""
    return render(request, 'home.html')
