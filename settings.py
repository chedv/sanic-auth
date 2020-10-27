from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config


app_settings = dict(host=config('APP_HOST', default='localhost'),
                    port=config('APP_PORT', default=8000, cast=int),
                    debug=config('APP_DEBUG', default=False, cast=bool))

db_settings = dict(user=config('DB_USER'),
                   password=config('DB_PASSWORD'),
                   host=config('DB_HOST', default='localhost'),
                   port=config('DB_PORT', default=5432, cast=int),
                   name=config('DB_NAME'))

db_connection = ('postgresql+psycopg2://'
                 '{user}:{password}@{host}:{port}/{name}').format(**db_settings)

db_engine = create_engine(db_connection, echo=True)

BaseModel = declarative_base()

Session = sessionmaker(bind=db_engine)

JWT_KEY = 'secret'
