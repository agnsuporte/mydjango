""" App Product
"""
from django.shortcuts import render


def index_product(request: any) -> render:
    """
    Return a list for products
    """
    return render(request, 'product/product_index.html')
