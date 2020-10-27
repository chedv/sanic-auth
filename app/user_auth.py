from app import serializers
from app import models
from app.database import Session

from settings import jwt_key
import jwt

import hashlib


def make_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


def authenticate(email, password):
    session = Session()
    user = session.query(models.User).filter_by(email=email).first()

    password_hash = make_password(password)
    if user.password_hash == password_hash:
        return user
    return None


def authorize(user):
    serializer = serializers.UserSerializer()
    json = serializer.dump(user)
    return jwt.encode(payload=json, key=jwt_key)
