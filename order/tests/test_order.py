import pytest
from django.contrib.auth.models import User

from order.models import Order
from product.models import Product


@pytest.mark.django_db
def test_create_order():
    # cria usuário
    user = User.objects.create_user(
        username="user_teste",
        password="123456"
    )

    # cria produto
    product = Product.objects.create(
        title="Produto Teste",
        description="Descrição Teste",
        price=100
    )

    # cria pedido
    order = Order.objects.create(user=user)
    order.product.add(product)

    # validações
    assert order.id is not None
    assert order.user == user
    assert order.product.count() == 1
    assert order.product.first() == product