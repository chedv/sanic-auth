from serializers import User, UserSerializer

from settings import Session, JWT_KEY
import jwt

import hashlib


def make_password(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


def authenticate(email, password):
    session = Session()
    user = session.query(User).filter_by(email=email).first()

    password_hash = make_password(password)
    if user.password_hash == password_hash:
        return user
    return None


def authorize(user):
    serializer = UserSerializer()
    json = serializer.dump(user)
    return jwt.encode(payload=json, key=JWT_KEY)
