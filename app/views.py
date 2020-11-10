from sanic.views import HTTPMethodView
from sanic import response

from app.forms import UserForm, ValidationError
from app.user_auth import register, authenticate, authorize, deauthorize
from app.decorators import login_required


class UserRegisterView(HTTPMethodView):
    async def post(self, request):
        user_form = UserForm()

        try:
            validated_data = user_form.load(request.json)
        except ValidationError as error:
            return response.json(error.messages, status=400)

        await register(validated_data)
        return response.empty(status=201)


class UserLoginView(HTTPMethodView):
    async def post(self, request):
        email = request.json['email']
        password = request.json['password']

        user = await authenticate(email, password)
        if user is None:
            return response.empty(status=404)

        token = await authorize(user)
        return response.json({'token': token.decode()})


class UserLogoutView(HTTPMethodView):
    @login_required
    async def post(self, request):
        user = request.args['user']
        await deauthorize(user)
        return response.empty(status=200)
