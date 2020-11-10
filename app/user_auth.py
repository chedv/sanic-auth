from app import serializers
from app import models
from app import user_session

from settings import jwt_key
from jwt import PyJWTError
import jwt

import hashlib


def register(user):
    models.User.add(user)


def make_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


def authenticate(email, password):
    query = models.User.query()
    user = query.filter_by(email=email).first()
    query.session.close()

    password_hash = make_password(password)
    if user is None or user.password_hash != password_hash:
        return None
    return user


def authorize(user):
    serializer = serializers.UserSerializer()
    data = serializer.dump(user)

    user_session.create_session(user)
    return jwt.encode(payload=data, key=jwt_key)


def deauthorize(user):
    user_session.delete_session(user)


def decode_token(token):
    try:
        data = jwt.decode(jwt=token, key=jwt_key)
    except PyJWTError:
        return None

    query = models.User.query()
    user = query.filter_by(**data).first()
    query.session.close()

    return user
