from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from store.order.models import Order


class PayOrder(ListView):
    model = Order
    template_name = 'order/index_order.html'
    context_object_name = 'Orders'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.order_by('id')
        print(query_set)
        return query_set


class OrderDetail(View):
    pass


class CloseOrder(View):
    pass
