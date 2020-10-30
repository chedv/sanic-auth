from tests.test_user_register_view import prepared_data
from tests.database import prepared_db, drop_db
from main import app

import pytest
import json


@pytest.fixture()
def prepared_register(prepared_db, prepared_data):
    data = json.dumps(prepared_data)
    app.test_client.post('/register', data=data)
    return prepared_data


def test_post_status_200(prepared_register):
    data = json.dumps(prepared_register)
    request, response = app.test_client.post('/login', data=data)
    assert response.status == 200

    drop_db()


def test_invalid_password(prepared_register):
    prepared_register['password'] = 'Qwerty1234'
    data = json.dumps(prepared_register)

    request, response = app.test_client.post('/login', data=data)
    assert response.status == 404

    drop_db()


def test_invalid_email(prepared_register):
    prepared_register['email'] = 'ivan.ivanov912@example.com'
    data = json.dumps(prepared_register)

    request, response = app.test_client.post('/login', data=data)
    assert response.status == 404

    drop_db()
