from flask import Flask

from db import db, base

from methods.coin import insert_coin


app = Flask(__name__)
app.debug = True


base.metadata.create_all(db)


@app.route("/coin/<name>", methods=["POST"])
def insert_coin_route(name):
    return insert_coin(name)


if __name__ == "__main__":
    app.run()
