from app.database import BaseModel
from sqlalchemy import Column, Integer, String

from app import user_auth


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = user_auth.make_password(password)
