from marshmallow import Schema, fields, post_load, ValidationError
from app import models


class UserSerializer(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return models.User(**data)
