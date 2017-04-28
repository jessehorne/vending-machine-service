import requests


ADDRESS = "http://localhost:5000"


def test_buy_product__exact_change():
    # insert exact change
    for x in xrange(4):
        r = requests.post(ADDRESS + "/coin/quarter")

        if not r.status_code == 200:
            assert False


    # attempt to buy
    r = requests.get(ADDRESS + "/product/cola")

    assert r.status_code == 200

    # make sure change was removed properly
    r = requests.get(ADDRESS + "/coin")

    assert r.json()["change"] == 0.0


def test_buy_product__invalid_change():
    # insert only a dime
    r = requests.post(ADDRESS + "/coin/dime")

    assert r.status_code == 200

    # attempt to purchase a cola
    r = requests.get(ADDRESS + "/product/cola")

    assert r.status_code == 400


def test_buy_product__more_change():
    # insert more than enough change
    for x in xrange(4):
        r = requests.post(ADDRESS + "/coin/quarter")

        assert r.status_code == 200

    for x in xrange(2):
        r = requests.post(ADDRESS + "/coin/dime")

        assert r.status_code == 200

    for x in xrange(2):
        r = requests.post(ADDRESS + "/coin/nickel")

        assert r.status_code == 200


    # attempt to buy a cola
    r = requests.get(ADDRESS + "/product/cola")

    assert r.status_code == 200
