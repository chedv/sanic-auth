from app import serializers
from app import models
from app import user_session

from settings import jwt_key
from jwt import PyJWTError
import jwt

import hashlib


async def register(user):
    await user.create()


def make_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


async def authenticate(email, password):
    user = await models.User.query.where(models.User.email == email).gino.first()

    password_hash = make_password(password)
    if user is None or user.password_hash != password_hash:
        return None
    return user


async def authorize(user):
    serializer = serializers.UserSerializer()
    data = serializer.dump(user)

    await user_session.create_session(user)
    return jwt.encode(payload=data, key=jwt_key)


async def deauthorize(user):
    await user_session.delete_session(user)


async def decode_token(token):
    try:
        data = jwt.decode(jwt=token, key=jwt_key)
    except PyJWTError:
        return None

    email = data['email']
    return await models.User.query.where(models.User.email == email).gino.first()
