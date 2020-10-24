from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from collections import namedtuple


AppSettings = namedtuple('AppSettings', ['host', 'port', 'debug'])

app_settings = AppSettings(host='localhost', port=8000, debug=True)

db_engine = create_engine('sqlite:///db.sqlite3', echo=True)

BaseModel = declarative_base()

Session = sessionmaker(bind=db_engine)

JWT_KEY = 'secret'
