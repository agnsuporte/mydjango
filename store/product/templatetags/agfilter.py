from django.template import Library
from utils import utils

register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco(val)


@register.filter
def quantity_total_car(car):
    return utils.quantity_total_car(car)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)
