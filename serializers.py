from marshmallow import Schema, fields, post_load
from models import User


class UserSerializer(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
