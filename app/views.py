from sanic.views import HTTPMethodView
from sanic import response

from app.database import Session
from app import session

from app.user_auth import authenticate, authorize
from app.serializers import UserSerializer, ValidationError


class UserRegisterView(HTTPMethodView):
    def post(self, request):
        serializer = UserSerializer()

        try:
            user = serializer.load(request.json)
        except ValidationError:
            return response.empty(status=404)

        session.add_entry(Session, entry=user)
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
