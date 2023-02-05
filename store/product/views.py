""" App Product
"""
from django.shortcuts import (
    render, HttpResponse, reverse, redirect, get_object_or_404
)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.http import JsonResponse

from store.product.models import Product, Variations
from utils.utils import quantity_total_car


class ProductList(ListView):
    model = Product
    paginate_by = 5
    template_name = 'product/product_index.html'
    context_object_name = 'Products'

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.order_by('id')
        print(query_set)
        return query_set


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'Product'
    slug_url_kwarg = 'slug'


class ProductAddCar(View):

    def post(self, *args, **kwargs):
        variation_id = self.request.POST.get('vid')

        if not variation_id:
            return JsonResponse({'message': 'Produto não existe'})

        variation = get_object_or_404(Variations, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id
        product_name = product.name
        variation_name = variation.name or ''
        price_product = float(variation.price)
        price_product_promotional = float(variation.price_promotional)
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock_min <= 1:
            return JsonResponse({'message': 'stock insuficiente'})

        if not self.request.session.get('sessionCar'):
            self.request.session['sessionCar'] = {}
            self.request.session.save()

        car = self.request.session['sessionCar']
        message = f'Produto: {product_name} / {variation_name} adicionado ao seu carrinho'

        if variation_id in car:
            quantityof_car = car[variation_id]['quantity']
            quantityof_car += 1

            if variation_stock < quantityof_car:
                message = f'Estoque insuficiente para {quantityof_car}x no '
                f'produto "{product_name}". Adicionamos {variation_stock}x no seu car.'

                quantityof_car = variation_stock

            car[variation_id]['quantity'] = quantityof_car
            car[variation_id]['price_total'] = price_product * quantityof_car
            car[variation_id]['price_total_promotional'] = price_product_promotional * quantityof_car
        else:
            car[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'price_product': price_product,
                'price_product_promotional': price_product_promotional,
                'price_total': price_product,
                'price_total_promotional': price_product_promotional,
                'quantity': 1,
                'slug': slug,
                'image': image,
            }

        self.request.session.save()

        qtde = quantity_total_car(car)

        return JsonResponse({'message': message, 'qtde': qtde})


class ProductRemoveCar(View):

    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product')
        )
        variacao_id = self.request.GET.get('vid')

        if not variacao_id:
            return redirect(http_referer)

        if not self.request.session.get('sessionCar'):
            return redirect(http_referer)

        if variacao_id not in self.request.session['sessionCar']:
            return redirect(http_referer)

        carrinho = self.request.session['sessionCar'][variacao_id]

        messages.success(
            self.request,
            f'Produto {carrinho["product_name"]} {carrinho["variation_name"]} '
            f'removido do seu carrinho.'
        )

        del self.request.session['sessionCar'][variacao_id]
        self.request.session.save()

        return redirect(http_referer)


class ProductCar(View):

    def get(self, *args, **kwargs):
        contexto = {
            'car': self.request.session.get('sessionCar', {})
        }

        return render(self.request, 'product/product_car.html', contexto)


class ProductCheckout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('ProductCheckout')
