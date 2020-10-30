from sanic import Sanic
from sanic import response
from sanic.views import HTTPMethodView
from app.routes import routes
from app.middlewares import middlewares
from settings import app_settings
from app.decorators import login_required

app = Sanic(__name__)


class View(HTTPMethodView):
    @login_required
    def get(self, request):
        return response.empty(status=200)


for route in routes:
    app.add_route(route.view, route.url)

app.add_route(View.as_view(), '/')

for middleware in middlewares:
    app.request_middleware.append(middleware)


if __name__ == '__main__':
    app.run(**app_settings)
