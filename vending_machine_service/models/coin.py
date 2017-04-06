import json

from sqlalchemy import Column, String, Float, Integer

from db import base


class Coin(base):
    __tablename__ = 'coins'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name})
