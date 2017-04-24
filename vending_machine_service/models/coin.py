import json

from sqlalchemy import Column, String, Float, Integer

from db import base


class Coin(base):
    __tablename__ = 'coins'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    worth = Column(Float)

    def __init__(self, name):
        self.name = name

        if self.name == "nickel":
            self.worth = 0.05
        elif self.name == "dime":
            self.worth = 0.1
        elif self.name == "quarter":
            self.worth = 0.25

    def __repr__(self):
        return json.dumps({"name": self.name, "worth": self.worth})
