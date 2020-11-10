from app.user_auth import decode_token
from app.user_session import get_session


async def jwt_authentication_middleware(request):
    user = None
    if request.token is not None:
        reviewed_user = await decode_token(request.token)
        session = await get_session(reviewed_user)
        if reviewed_user is not None and session is not None:
            user = reviewed_user

    request.args['user'] = user


middlewares = (
    jwt_authentication_middleware,
)
