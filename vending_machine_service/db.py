from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


db = create_engine('sqlite:////tmp/tmp.db')
db.echo = True

base = declarative_base()
