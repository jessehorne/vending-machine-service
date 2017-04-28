from mock import MagicMock

from vending_machine_service.methods.product import (reload_stock,
                                                     get_product_cost,
                                                     remove_one,
                                                     buy_product)


def test_reload_stock():
    session = MagicMock()

    session.query().delete.return_value = None
    session.commit.return_value = None
    session.add.return_value = None

    assert reload_stock(session)


def test_get_product_cost():
    test_product = MagicMock()
    test_product.price = 0.0

    session = MagicMock()

    session.query().filter_by().first.return_value = test_product

    assert get_product_cost(session, "nickel") == 0.0


def test_remove_one__amount_more_than_zero():
    test_product = MagicMock()
    test_product.amount = 5

    session = MagicMock()
    session.query().filter_by().first.return_value = test_product

    assert remove_one(session, "nickel")


def test_remove_one__amount_is_zero():
    test_product = MagicMock()
    test_product.amount = 0

    session = MagicMock()
    session.query().filter_by().first.return_value = test_product

    assert not remove_one(session, "nickel")


def test_buy_product__not_existing_product():
    session = MagicMock()
    session.query().all.return_value = []
    session.query().filter_by().first.return_value = None

    bought, data = buy_product(session, "invalid_product_name")

    assert not bought and data == {"display": "INVALID PRODUCT"}


def test_buy_product__existing_product__not_enough_inserted_coins():
    test_product_to_buy = MagicMock()
    test_product_to_buy.worth = 0.25

    test_product = MagicMock()
    test_product.price = 1.0

    session = MagicMock()
    session.query().all.return_value = [test_product_to_buy]
    session.query().filter_by().first.return_value = test_product

    bought, data = buy_product(session, "cola")

    assert not bought and data == {"display": "INSERT COINS"}


def test_buy_product__existing_product__exactly_enough_inserted_coins():
    test_product_to_buy = MagicMock()
    test_product_to_buy.worth = 1.0

    test_product = MagicMock()
    test_product.price = 1.0

    session = MagicMock()
    session.query().all.return_value = [test_product_to_buy]
    session.query().filter_by().first.return_value = test_product

    bought, data = buy_product(session, "cola")

    assert bought and data == {"product": "cola"}


def test_buy_product__existing_product__more_inserted_coins_than_price():
    bought_product = {
        "product": "cola",
        "coins": [0.25, 0.25, 0.25, 0.25]
    }

    test_product_to_buy = MagicMock()
    test_product_to_buy.worth = 2.0

    test_product = MagicMock()
    test_product.price = 1.0

    session = MagicMock()
    session.query().all.return_value = [test_product_to_buy]
    session.query().filter_by().first.return_value = test_product

    bought, data = buy_product(session, "cola")

    assert bought and data == bought_product
