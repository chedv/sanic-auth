# sanic-auth

Example authentication project based on Sanic

# Installation and launching

Clone project:

```shell script
git clone https://github.com/chedv/sanic-auth.git
cd sanic-auth
```

Create virtual environment and install dependencies:

```shell script
python3.8 -m venv <venv name>
python3.8 -m pip install -r requirements.txt
```

For database configuration, you should add .env file:

```.env

# Database variables
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_NAME=<db_name>

```

Also you can change default configuration variables:

```.env
# Application variables
APP_HOST=localhost
APP_PORT=8000
APP_DEBUG=True

# Database variables
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=localhost
DB_PORT=5432
DB_NAME=<db_name>

JWT_KEY=<jwt secret key>
```

Run project:

```shell script
python3.8 main.py
```

Run tests:

```shell script
python3.8 -m pytest
```