from app import serializers
from app import models
from app.user_session import create_session

from settings import jwt_key
import jwt

import hashlib


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

    create_session(user)
    return jwt.encode(payload=data, key=jwt_key)


def decode_token(token):
    data = jwt.decode(jwt=token, key=jwt_key)

    query = models.User.query()
    user = query.filter_by(**data).first()
    query.session.close()

    return user
