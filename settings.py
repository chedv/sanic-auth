from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app_settings = dict(host='localhost', port=8000, debug=True)

db_settings = dict(type='postgresql', driver='psycopg2',
                   user='che', password='sanicauth',
                   host='localhost', port=5432, name='userdb')

db_connection = '{type}+{driver}://{user}:{password}@{host}:{port}/{name}'.format(**db_settings)

db_engine = create_engine(db_connection, echo=True)

BaseModel = declarative_base()

Session = sessionmaker(bind=db_engine)

JWT_KEY = 'secret'
