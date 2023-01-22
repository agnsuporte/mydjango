from django.shortcuts import render

# Create your views here. index_order


def index_order(request: any) -> render:
    """
    Return order
    """
    return render(request, 'order/index_order.html')
