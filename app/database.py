from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import db_settings


db_connection = ('postgresql+psycopg2://'
                 '{user}:{password}@{host}:{port}/{name}').format(**db_settings)

db_engine = create_engine(db_connection, echo=True)

BaseModel = declarative_base()

Session = sessionmaker(bind=db_engine)
