import pytest

from product.models import Category


@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(
        title="Eletrônicos",
        slug="eletronicos",
        description="Categoria de produtos eletrônicos",
        active=True
    )

    assert category.id is not None
    assert category.title == "Eletrônicos"
    assert category.slug == "eletronicos"
    assert category.description == "Categoria de produtos eletrônicos"
    assert category.active is True