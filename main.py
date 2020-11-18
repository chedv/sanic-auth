from app.app import SanicServer
from settings import app_settings


if __name__ == '__main__':
    app = SanicServer(__name__)
    app.load_api()
    app.run(**app_settings)
