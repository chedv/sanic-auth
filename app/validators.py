from marshmallow import ValidationError
from string import punctuation, ascii_uppercase, digits


uppercases = frozenset(ascii_uppercase)
digits = frozenset(digits)
symbols = frozenset(punctuation)


def contains_one_char(str_val, chars):
    for char in str_val:
        if char in chars:
            return True
    return False


def validate_password(password):
    if not contains_one_char(password, uppercases):
        raise ValidationError('Password must contain at least one uppercase symbol')

    if not contains_one_char(password, digits):
        raise ValidationError('Password must contain at least one digit symbol')

    if not contains_one_char(password, symbols):
        raise ValidationError('Password must contain at least one special symbol')
