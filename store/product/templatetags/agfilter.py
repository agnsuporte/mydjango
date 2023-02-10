from django.template import Library
from utils import utils

register = Library()


@register.filter
def format_price(val):
    return utils.format_price(val)


@register.filter
def quantity_total_car(car):
    return utils.quantity_total_car(car)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)
