from tests.database import prepared_db, drop_db
from main import app

import pytest
import json


@pytest.fixture()
def prepared_data():
    return dict(email='ivan.ivanov911@example.com', password='Qwerty123')


def test_post_created_status(prepared_db, prepared_data):
    data = json.dumps(prepared_data)
    request, response = app.test_client.post('/register', data=data)
    assert response.status == 201
    drop_db()


def test_not_allowed_methods():
    methods = ('get', 'put', 'delete', 'patch', 'options', 'head')
    for method in methods:
        request, response = getattr(app.test_client, method)('/register')
        assert response.status == 405


def test_invalid_email(prepared_data):
    invalid_emails = ('ivan.ivanov911', 'ivan.ivanov911@', '@example.com')
    for email in invalid_emails:
        prepared_data['email'] = email
        data = json.dumps(prepared_data)

        request, response = app.test_client.post('/register', data=data)
        assert response.status == 404
