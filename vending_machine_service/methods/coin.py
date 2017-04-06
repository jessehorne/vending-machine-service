from util import get_session, response

from models.coin import Coin


coins = ["nickle", "dime", "quarter"]


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
