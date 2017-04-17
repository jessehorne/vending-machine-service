from flask import Flask

from db import db, base

from methods.coin import (get_coins, insert_coin, delete_all_coins)


app = Flask(__name__)
app.debug = True


base.metadata.create_all(db)


@app.route("/coin", methods=["GET"])
def get_coins_route():
    return get_coins()


@app.route("/coin", methods=["DELETE"])
def delete_all_coins_route():
    return delete_all_coins()
    

@app.route("/coin/<name>", methods=["POST"])
def insert_coin_route(name):
    return insert_coin(name)


if __name__ == "__main__":
    app.run()
