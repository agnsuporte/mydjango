from django.db import models
from django.contrib.auth.models import User

"""

Classe de Pedidos
"""


class Order(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        default='P',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Order No. {self.pk}'


"""

Classe de Itens do Pedido
"""


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    prodct_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_promotional = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    quantity_of = models.PositiveIntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return f'Item {self.order}'
