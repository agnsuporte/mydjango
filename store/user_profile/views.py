""" App Profile
"""
from django.shortcuts import render


def index_profile(request: any) -> render:
    """
    Return a list for products
    """
    return render(request, 'user_profile/index_profile.html')
