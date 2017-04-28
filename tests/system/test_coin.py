import requests


ADDRESS = "http://localhost:5000"


def test_insert_coins__valid_coins():
    # test valid coins
    coins = ["nickel", "dime", "quarter"]

    for coin in coins:
        r = requests.post(ADDRESS + "/coin/{}".format(coin))

        if not r.status_code == 200:
            assert False

    r = requests.delete(ADDRESS + "/coin")


def test_insert_coins__invalid_coin():
    invalid_coins = ["penny", "super coin", "mega super coin"]

    for invalid_coin in invalid_coins:
        r = requests.post(ADDRESS + "/coin/{}".format(invalid_coin))

        if not r.status_code == 400:
            assert False


def test_display__no_coins():
    r = requests.get(ADDRESS + "/coin")

    assert r.json()["change"] == 0.0


def test_display__existing_coin():
    coins = ["nickel", "dime", "quarter"]

    for coin in coins:
        r = requests.post(ADDRESS + "/coin/{}".format(coin))

        if not r.status_code == 200:
            assert False


    r = requests.get(ADDRESS + "/coin")

    assert "INSERT COINS" not in r.text

    r = requests.delete(ADDRESS + "/coin")

    assert r.status_code == 200
