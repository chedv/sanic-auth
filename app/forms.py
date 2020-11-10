from marshmallow import Schema, fields, validate, ValidationError
from app.validators import validate_password


class UserForm(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    username = fields.String(required=True,
                             validate=[validate.Regexp(r'^[a-zA-Z0-9._-]+$'),
                                       validate.Length(min=3, max=20)])
    password = fields.String(required=True,
                             validate=[validate_password,
                                       validate.Length(min=8)])
