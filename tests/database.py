from sqlalchemy import create_engine
from app.database import Base, DBSession

import pytest

db_engine = create_engine('sqlite:///:memory:', echo=True)


@pytest.fixture()
def prepared_db():
    DBSession.configure(bind=db_engine)
    Base.metadata.create_all(db_engine)


def drop_db():
    Base.metadata.drop_all(db_engine)
