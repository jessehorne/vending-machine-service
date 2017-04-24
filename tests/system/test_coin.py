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


def test_display__no_coins():
    r = requests.get(ADDRESS + "/coin")

    assert "INSERT COINS" in r.text


def test_display__existing_coin():
    coins = ["nickel", "dime", "quarter"]

    for coin in coins:
        r = requests.post(ADDRESS + "/coin/{}".format(coin))

        if not r.status_code == 200:
            assert False


    r = requests.get(ADDRESS + "/coin")

    assert "INSERT COINS" not in r.text

    r = requests.delete(ADDRESS + "/coin")
