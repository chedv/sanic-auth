from sanic.views import HTTPMethodView
from sanic import response

from serializers import UserSerializer
from models import User
from settings import Session, JWT_KEY

import jwt


class UserRegisterView(HTTPMethodView):
    def post(self, request):
        serializer = UserSerializer()
        user = serializer.load(request.json)

        session = Session()
        session.add(user)
        session.commit()

        return response.empty(status=201)


class UserLoginView(HTTPMethodView):
    def post(self, request):
        return response.json({'token': ''})
