from app.views import UserRegisterView, UserLoginView
from collections import namedtuple


Route = namedtuple('Route', ['view', 'url'])

routes = [
    Route(view=UserRegisterView.as_view(), url='/register'),
    Route(view=UserLoginView.as_view(), url='/login'),
]
