from app.tables import UserTable
from app import user_session

from settings import jwt_key
from jwt import PyJWTError
import jwt

import hashlib


async def register(validated_data):
    row = dict()

    for key, value in validated_data.items():
        if key == 'password':
            row['password_hash'] = make_password(value)
        else:
            row[key] = value

    await UserTable.add_row(row)


def make_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


async def authenticate(email, password):
    row = await UserTable.get_row(UserTable.c.email, email)

    password_hash = make_password(password)
    if not row or row['password_hash'] != password_hash:
        return None
    return row


async def authorize(user):
    await user_session.create_session(user)
    return jwt.encode(payload=dict(user), key=jwt_key)


async def deauthorize(user):
    await user_session.delete_session(user)


async def decode_token(token):
    try:
        data = jwt.decode(jwt=token, key=jwt_key)
    except PyJWTError:
        return None

    row = await UserTable.get_row(UserTable.c.email, data['email'])
    return row if row else None
