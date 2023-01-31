
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


def quantity_total_car(car):
    return sum([item['quantity'] for item in car.values()])


def cart_totals(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()
        ]
    )
