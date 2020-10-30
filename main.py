from sanic import Sanic
from app.routes import routes
from app.middlewares import middlewares
from settings import app_settings

app = Sanic(__name__)

for route in routes:
    app.add_route(route.view, route.url)

for middleware in middlewares:
    app.request_middleware.append(middleware)


if __name__ == '__main__':
    app.run(**app_settings)
