from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from flask import jsonify

from db import db


session = sessionmaker(bind=db)()


@contextmanager
def get_session():
    yield session


def response(status=200, data={}):
    res = jsonify(data)
    res.status_code = status

    return res
