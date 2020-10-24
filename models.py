from settings import BaseModel
from sqlalchemy import Column, Integer, String

import hashlib


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = User.make_password(password)

    @staticmethod
    def make_password(raw_password):
        return hashlib.sha256(raw_password.encode()).hexdigest()
