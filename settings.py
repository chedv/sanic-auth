from decouple import config


app_settings = dict(host=config('APP_HOST', default='localhost'),
                    port=config('APP_PORT', default=8000, cast=int),
                    debug=config('APP_DEBUG', default=False, cast=bool))

db_settings = dict(user=config('DB_USER'),
                   password=config('DB_PASSWORD'),
                   host=config('DB_HOST', default='localhost'),
                   port=config('DB_PORT', default=5432, cast=int),
                   name=config('DB_NAME'))

jwt_key = config('JWT_KEY', default='secret')
