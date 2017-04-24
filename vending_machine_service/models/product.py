import json

from sqlalchemy import Column, String, Float, Integer

from db import base


class Product(base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)

    def __repr__(self):
        return json.dumps({"id": self.id, "name": self.name,
                           "price": self.price, "amount": self.amount})
