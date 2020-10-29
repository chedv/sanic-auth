from app.database import Base, session_factory
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app import user_auth


class BaseModel:
    @staticmethod
    def add(instance):
        session = session_factory()
        session.add(instance)
        session.commit()

    @staticmethod
    def delete(instance):
        session = session_factory()
        session.delete(instance)
        session.commit()

    @classmethod
    def query(cls):
        return session_factory().query(cls)


class User(Base, BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String(64), nullable=False)

    session = relationship('Session', back_populates='user', uselist=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = user_auth.make_password(password)


class Session(Base, BaseModel):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='session')
