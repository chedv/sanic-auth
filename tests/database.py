from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import BaseModel

import pytest


db_engine = create_engine('sqlite:///:memory:', echo=True)

Session = sessionmaker(bind=db_engine)


def add_entry(session_cls, entry):
    session = Session()
    session.add(entry)
    session.commit()


def create_query(session_cls):
    session = Session()
    return session.query


@pytest.fixture()
def prepared_db(mocker):
    mocker.patch('app.session.add_entry', side_effect=add_entry)
    mocker.patch('app.session.create_query', side_effect=create_query)

    BaseModel.metadata.create_all(db_engine)


def drop_db():
    BaseModel.metadata.drop_all(db_engine)
