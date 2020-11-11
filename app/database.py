from gino.ext.sanic import Gino

from settings import db_settings


db = Gino()


def db_connection(app):
    app.config.DB_USER = db_settings['user']
    app.config.DB_PASSWORD = db_settings['password']
    app.config.DB_HOST = db_settings['host']
    app.config.DB_PORT = db_settings['port']
    app.config.DB_DATABASE = db_settings['database']

    db.init_app(app)
