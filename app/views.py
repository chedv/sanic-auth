from sanic.views import HTTPMethodView
from sanic import response

from app.serializers import UserSerializer, ValidationError
from app.user_auth import register, authenticate, authorize, deauthorize
from app.decorators import login_required


class UserRegisterView(HTTPMethodView):
    def post(self, request):
        serializer = UserSerializer()

        try:
            user = serializer.load(request.json)
        except ValidationError as error:
            return response.json(error.messages, status=400)

        register(user)
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
    @login_required
    def post(self, request):
        user = request.args['user']
        deauthorize(user)
        return response.empty(status=200)
