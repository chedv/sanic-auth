from app.user_session import get_session
from app import responses


def login_required(handler):
    async def wrapper(self, request):
        user = request.args['user']
        if user is None:
            return responses.unauthorized
        if await get_session(user) is None:
            return responses.unauthorized
        return await handler(self, request)
    return wrapper
