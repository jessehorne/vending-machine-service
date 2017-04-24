import json

from util import get_session, response

from models.coin import Coin


coins = ["nickle", "dime", "quarter"]


def get_coins():
    with get_session() as session:
        all_coins = session.query(Coin).all()

        if len(all_coins) == 0:
            return response(status=200, data={"msg": "INSERT COINS"})
        else:
            json_coins = [json.loads(str(c)) for c in all_coins]
            return response(status=200, data={"coins": json_coins})

        return response(status=200, data=coin_data)


def insert_coin(name):
    if name in coins:
        with get_session() as session:
            new_coin = Coin(name=name)

            session.add(new_coin)
            session.commit()

            return response(status=200, data={})
    else:
        data = {
            "message": "That coin isn't accepted."
        }

        return response(status=400, data=data)


def delete_all_coins():
    with get_session() as session:
        session.query(Coin).delete()

        return response(status=200, data={})
