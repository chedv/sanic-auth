from app.user_session import get_session
from sanic.exceptions import abort


def login_required(handler):
    def wrapper(self, request):
        user = request.args['user']
        if user is None:
            abort(status_code=401)
        if get_session(user) is None:
            abort(status_code=401)
        return handler(self, request)
    return wrapper
