import json
import itertools

from util import get_session, response

from models.product import Product
from models.coin import Coin

from methods.coin import get_coin_amount


def reload_stock(session):
    # this is dirty, in the future, please use alembic or something
    existing_product = session.query(Product).delete()
    existing_coin = session.query(Coin).delete()

    session.commit()

    new_cola = Product(name="cola", price=1.0, amount=1)
    new_chips = Product(name="chips", price=0.5, amount=1)
    new_candy =  Product(name="candy", price=0.65, amount=1)

    session.add(new_cola)
    session.add(new_chips)
    session.add(new_candy)

    session.commit()

    return True


def get_product_cost(session, name):
    p = session.query(Product).filter_by(name=name).first()

    if p:
        return p.price


def remove_one(session, name):
    p = session.query(Product).filter_by(name=name).first()

    if p.amount > 0:
        p.amount -= 1

        session.commit()

        return True


def buy_product(session, name):
    coin_amt = get_coin_amount(session)
    price = get_product_cost(session, name)

    existing_product = session.query(Product).filter_by(name=name).first()

    if not existing_product:
        return False, {"display": "INVALID PRODUCT"}

    if coin_amt < price:
        return False, {"display": "INSERT COINS"}
    elif coin_amt == price:
        remove_one(session, name)

        session.query(Coin).delete()

        return True, {"product": name}
    else:
        coins = [0.25, 0.1, 0.05]
        current_coin = 0

        return_coins = coin_amt - price

        return_coins_i = 0

        coins_used = []

        while return_coins_i != return_coins:
            if current_coin == len(coins):
                break

            temp_return_coins = return_coins_i + coins[current_coin]

            if temp_return_coins > return_coins:
                current_coin += 1
            else:
                coins_used += [coins[current_coin]]
                return_coins_i = return_coins_i + coins[current_coin]

        session.query(Coin).delete()

        data = {
            "product": name,
            "coins": coins_used,
        }

        return True, data
