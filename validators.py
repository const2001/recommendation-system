from jsonschema import validate, ValidationError
from schemas import user_schema, event_schema, coupon_schema


def validate_user(user):
    try:
        validate(user, user_schema)
        return True,"The JSON data is valid."
    except ValidationError as e:
        return False,"The JSON data is not valid. " + str(e)


def validate_event(event):
    try:
        validate(event, event_schema)
        return True,"The JSON data is valid."
    except ValidationError as e:
        return False,"The JSON data is not valid. " + str(e)

def validate_coupon(coupon):
    try:
        validate(coupon, coupon_schema)
        return True,"The JSON data is valid."
    except ValidationError as e:
        return False,"The JSON data is not valid. " + str(e)
