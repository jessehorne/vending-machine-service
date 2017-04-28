import json

from util import get_session, response

from models.coin import Coin


coins = ["nickel", "dime", "quarter"]


def get_coin_amount(session):
    current_coins = session.query(Coin).all()
    current_count = 0.0

    for c in current_coins:
        current_count += c.worth

    return current_count


def insert_coin(session, name):
    if name in coins:
        new_coin = Coin(name=name)

        session.add(new_coin)
        session.commit()

        return True


def delete_all_coins(session):
    session.query(Coin).delete()

    return True
