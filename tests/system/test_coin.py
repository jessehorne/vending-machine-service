import requests


ADDRESS = "http://localhost:5000"


def test_insert_coins__valid_coins():
    # test valid coins
    coins = ["nickle", "dime", "quarter"]

    for coin in coins:
        r = requests.post(ADDRESS + "/coin/{}".format(coin))

        if not r.status_code == 200:
            assert False
