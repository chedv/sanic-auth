from sanic import Sanic
from app.routes import routes
from settings import app_settings

app = Sanic(__name__)

for route in routes:
    app.add_route(route.view, route.url)

if __name__ == '__main__':
    app.run(**app_settings)
