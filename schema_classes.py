from datetime import datetime
from marshmallow import Schema, fields ,ValidationError

class UserSchema(Schema):
    birth_year = fields.Integer(required=True)
    country = fields.String(required=True)
    currency = fields.String(required=True)
    gender = fields.String(required=True)
    sport_pref = fields.String(required=True)
    registration_date = fields.DateTime(required=True)

class EventSchema(Schema):
    begin_timestamp = fields.DateTime(required=True)
    country = fields.String(required=True)
    end_timestamp = fields.DateTime(required=True)
    event_id = fields.UUID(required=True)
    league = fields.String(required=True)
    participants = fields.List(fields.String(), required=True)
    sport = fields.String(required=True)


class SelectionSchema(Schema):
    event_id = fields.UUID(required=True)
    odds = fields.Float(required=True)

class CouponSchema(Schema):
    coupon_id = fields.UUID(required=True)
    selections = fields.List(fields.Nested(SelectionSchema), required=True)
    stake = fields.Float(required=True)
    timestamp = fields.DateTime(required=True)
    user_id = fields.Integer(required=True)    

