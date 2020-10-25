from sanic.views import HTTPMethodView
from sanic import response

from settings import Session

from user_auth import UserSerializer, authenticate, authorize
from serializers import ValidationError


class UserRegisterView(HTTPMethodView):
    def post(self, request):
        serializer = UserSerializer()

        try:
            user = serializer.load(request.json)
        except ValidationError:
            return response.empty(status=404)

        session = Session()
        session.add(user)
        session.commit()

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
