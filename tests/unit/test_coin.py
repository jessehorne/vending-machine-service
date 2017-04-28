from mock import MagicMock

from vending_machine_service.methods.coin import (get_coin_amount, insert_coin,
                                                  delete_all_coins)


def test_get_coin_amount():
    session = MagicMock()
    session.query().all.return_value = []

    coin_amount = get_coin_amount(session)

    assert coin_amount == 0.0


def test_insert_coin__valid_name():
    session = MagicMock()
    session.add = lambda x : None
    session.commit = lambda : None

    assert insert_coin(session, "nickel")


def test_insert_coin__invalid_name():
    session = MagicMock()
    session.add = lambda x : None
    session.commit = lambda : None

    assert not insert_coin(session, "invalid_coin_name")


def test_delete_all_coins():
    session = MagicMock()
    session.query().delete.return_value = None

    assert delete_all_coins(session)
