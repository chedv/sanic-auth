from sanic.views import HTTPMethodView
from sanic import response

from app.serializers import UserSerializer, ValidationError
from app.user_auth import authenticate, authorize
from app.user_session import delete_session
from app import models


class UserRegisterView(HTTPMethodView):
    def post(self, request):
        serializer = UserSerializer()

        try:
            user = serializer.load(request.json)
        except ValidationError as error:
            return response.json(error.messages, status=400)

        models.User.add(user)
        return response.empty(status=201)


class UserLoginView(HTTPMethodView):
    def post(self, request):
        email = request.json['email']
        password = request.json['password']

        user = authenticate(email, password)
        if user is None:
            return response.empty(status=404)

        token = authorize(user).decode()
        return response.json({'token': token})


class UserLogoutView(HTTPMethodView):
    def post(self, request):
        user = request.args['user']
        if user is None:
            return response.empty(status=400)

        delete_session(user)
        return response.empty(status=200)
