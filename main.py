from sanic import Sanic

from routes import routes
from settings import app_settings


if __name__ == '__main__':
    app = Sanic(__name__)

    for route in routes:
        app.add_route(route.view, route.url)

    app.run(**app_settings)
