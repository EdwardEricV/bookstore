import pytest

from product.models import Product, Category


@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(
        title="Livros",
        slug="livros"
    )

    product = Product.objects.create(
        title="Livro Django",
        description="Livro sobre Django",
        price=150,
        active=True
    )

    product.category.add(category)

    assert product.id is not None
    assert product.title == "Livro Django"
    assert product.description == "Livro sobre Django"
    assert product.price == 150
    assert product.active is True
    assert product.category.count() == 1
    assert product.category.first() == category