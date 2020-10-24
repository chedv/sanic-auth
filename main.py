from sanic import Sanic

from routes import routes
from settings import app_settings


if __name__ == '__main__':
    app = Sanic(__name__)

    for route in routes:
        app.add_route(route.view, route.url)

    app.run(host=app_settings.host, port=app_settings.port, debug=app_settings.debug)
