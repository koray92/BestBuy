import pytest
from products import Product

def test_create_product():
    assert Product("Test", price= 500, quantity=50).active == True


def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", price=100, quantity=200)


def test_product_inactive():
    assert Product("abc", price=50, quantity=0).is_active() == False


def test_purchase_quantity():
    assert Product("abc", price=50, quantity=10).buy(10)



def test_purchase_larger_quantity():
    assert Product("abc", price=50, quantity=10).buy(15)


pytest.main()