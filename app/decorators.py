from app.user_session import get_session
from app import responses


def login_required(handler):
    def wrapper(self, request):
        user = request.args['user']
        if user is None:
            return responses.unauthorized
        if get_session(user) is None:
            return responses.unauthorized
        return handler(self, request)
    return wrapper
