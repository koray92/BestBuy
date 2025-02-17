import pytest
from products import Product

def test_create_product():
    assert Product("Test", price= 500, quantity=50).active == True


def test_create_invalid_product():
    with pytest.raises(Product("", price=100, quantity=200):
        return ValueError
    with pytest.raises(Product("test", price=-100, quantity=50):
        return ValueError
    with pytest.raises(Product("test1", price=250, quantity=-20):
        return ValueError


def test_product_inactive():
    assert Product("abc", price=50, quantity=0).is_active() == False


def test_purchase_quantity():
    assert Product("abc", price=50, quantity=10).buy(10)
    assert Product.get_quantity()


def test_purchase_larger_quantity():
    pass

pytest.main()