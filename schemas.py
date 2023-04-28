#User Schema:
user_schema = {
    "type": "object",
    "properties": {
        "birth_year": {"type": "integer"},
        "country": {"type": "string"},
        "currency": {"type": "string"},
        "registration_date": {"type": "string", "format": "date-time"},
        "user_id": {"type": "integer"},
        "sport_pref": {"type": "string"}
    },
    "required": ["birth_year", "country", "currency", "registration_date", "user_id","sport_pref"]
}

#Event Schema:
event_schema={
    "type": "object",
    "properties": {
        "begin_timestamp": {"type": "string", "format": "date-time"},
        "country": {"type": "string"},
        "end_timestamp": {"type": "string", "format": "date-time"},
        "event_id": {"type": "string"},
        "league": {"type": "string"},
        "participants": {"type": "array", "items": {"type": "string"}},
        "sport": {"type": "string"}
    },
    "required": ["begin_timestamp", "country", "end_timestamp", "event_id", "league", "participants", "sport"]
}

#Coupon Schema:
coupon_schema={
    "type": "object",
    "properties": {
        "coupon_id": {"type": "string"},
        "selections": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "event_id": {"type": "string"},
                    "odds": {"type": "number"}
                },
                "required": ["event_id", "odds"]
            }
        },
        "stake": {"type": "number"},
        "timestamp": {"type": "string", "format": "date-time"},
        "user_id": {"type": "integer"}
    },
    "required": ["coupon_id", "selections", "stake", "timestamp", "user_id"]
}