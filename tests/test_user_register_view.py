from tests.database import prepared_db, drop_db
from main import app

import pytest
import json


@pytest.fixture()
def prepared_data():
    return dict(email='ivan.ivanov911@example.com',
                username='ivan.ivanov911',
                password='Qwerty12@')


def test_post_created_status(prepared_db, prepared_data):
    data = json.dumps(prepared_data)
    request, response = app.test_client.post('/register', data=data)
    assert response.status == 201
    drop_db()


def test_invalid_email(prepared_data):
    invalid_emails = ('ivan.ivanov911', 'ivan.ivanov911@', '@example.com')
    for email in invalid_emails:
        prepared_data['email'] = email
        data = json.dumps(prepared_data)

        request, response = app.test_client.post('/register', data=data)
        assert response.status == 400


def test_invalid_username(prepared_data):
    invalid_usernames = ('iv', 'iv$', 'iva@', 'ivanivanivanivanivani')
    for username in invalid_usernames:
        prepared_data['username'] = username
        data = json.dumps(prepared_data)

        request, response = app.test_client.post('/register', data=data)
        assert response.status == 400


def test_invalid_password(prepared_data):
    invalid_passwords = ('Qwert1#', 'Qwerty12', 'qwerty12#', 'Qwerty##')
    for password in invalid_passwords:
        prepared_data['password'] = password
        data = json.dumps(prepared_data)

        request, response = app.test_client.post('/register', data=data)
        assert response.status == 400
