from tests.test_user_login_view import prepared_data, prepared_register
from tests.database import prepared_db, drop_db
from main import app

import pytest
import json


@pytest.fixture()
def prepared_login(prepared_db, prepared_register):
    data = json.dumps(prepared_register)
    request, response = app.test_client.post('/login', data=data)
    return prepared_register, json.loads(response.body)


def auth_header(token_dict):
    token = token_dict['token']
    return {"Authorization": f"Token {token}"}


def logout(token_dict):
    return app.test_client.post('/logout', headers=auth_header(token_dict))


def test_logout(prepared_login):
    user_dict, token_dict = prepared_login

    request, response = logout(token_dict)
    assert response.status == 200

    request, response = logout(token_dict)
    assert response.status == 401

    drop_db()


def test_invalid_token(prepared_login):
    invalid_token_dict = {
        'token': ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ0b3B0YWwuY29tIiwiZXhwIjoxN'
                  'DI2NDIwODAwLCJodHRwOi8vdG9wdGFsLmNvbS9qd3RfY2xhaW1zL2lzX2FkbWluIjp0cnVlLCJ'
                  'jb21wYW55IjoiVG9wdGFsIiwiYXdlc29tZSI6dHJ1ZX0.yRQYnWzskCZUxPwaQupWkiUzKELZ4'
                  '9eM7oWxAQK_ZXw')
    }

    request, response = logout(invalid_token_dict)
    assert response.status == 401

    drop_db()
