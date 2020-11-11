from app.database import db
from app import user_auth


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String(64), nullable=False)


def create_user(email, username, password):
    password_hash = user_auth.make_password(password)
    return User(email=email, username=username, password_hash=password_hash)


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(None, db.ForeignKey('users.id'))
