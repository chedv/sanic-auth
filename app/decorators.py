from app.user_session import get_session
from sanic import response


def unauthorized_response():
    error_msg = {'detail': 'Authentication credentials were not provided.'}
    return response.json(error_msg, status=401)


def login_required(handler):
    def wrapper(self, request):
        user = request.args['user']
        if user is None:
            return unauthorized_response()
        if get_session(user) is None:
            return unauthorized_response()
        return handler(self, request)
    return wrapper
