from flask import Flask

from db import db, base

from methods.coin import (get_coin_amount, insert_coin, delete_all_coins)
from methods.product import (reload_stock, buy_product)

from util import response, get_session

app = Flask(__name__)
app.debug = True


base.metadata.create_all(db)


# add default stock
with app.test_request_context():
    with get_session() as session:
        reload_stock(session)


@app.route("/coin", methods=["GET"])
def get_coins_route():
    with get_session() as session:
        data = {"change": get_coin_amount(session)}

    return response(status=200, data=data)


@app.route("/coin", methods=["DELETE"])
def delete_all_coins_route():
    with get_session() as session:
        delete_all_coins(session)

    return response(status=200, data={})


@app.route("/coin/<name>", methods=["POST"])
def insert_coin_route(name):
    with get_session() as session:
        inserted = insert_coin(session, name)

    if not inserted:
        return response(status=400, data={"msg": "Failed to insert coin."})

    return response(status=200, data=inserted)


@app.route("/product/<name>", methods=["GET"])
def buy_product_route(name):
    with get_session() as session:
        bought, data = buy_product(session, name)

    if bought is True:
        return response(status=200, data=data)
    else:
        return response(status=400, data=data)


if __name__ == "__main__":
    app.run()
