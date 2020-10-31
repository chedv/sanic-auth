# sanic-auth

Example authentication project based on Sanic

# Installation and launching

Clone project:

```shell
git clone https://github.com/chedv/sanic-auth.git
cd sanic-auth
```

Create virtual environment and install dependencies:

```shell
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

Also you can change other configuration variables, here is an example of the file with all variables:

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

After that you should apply migrations by using ``liquibase``, so you need to install it and ``PostgreSQL JDBC Driver``. After installing you should create ``liquibase.properties`` file in migrations folder:

```.env
driver=org.postgresql.Driver
url=jdbc:postgresql://localhost:5432/<db_name>
username=<db_user>
password=<db_password>
```

Applying migrations are executed by following commands:

```shell
liquibase --changeLogFile=users_changelog.sql update
liquibase --changeLogFile=sessions_changelog.sql update
```

Finally, you can run project:

```shell
python3.8 main.py
```

Also you can run tests:

```shell
python3.8 -m pytest
```