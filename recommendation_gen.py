from datetime import datetime, timezone



# Recommend events based on user preferences
def recommend_events(user_id, events):
    user_pref = user_preferences[user_id]
    recommended_events = []
    for event in events:
        if event["country"] == user_pref["country"] and event["sport"] == user_pref["sport"]:
            recommended_events.append(event)
    return recommended_events

# User data
users = [
    {"user_id": 1, "birth_year": 1990, "country": "Italy", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"},
    {"user_id": 2, "birth_year": 1985, "country": "Germany", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"},
    {"user_id": 3, "birth_year": 1995, "country": "Spain", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"}
]

# Event data
events = [
    {"event_id": "E001", "league": "Premier League", "sport": "Football", "country": "England", "begin_timestamp": "2022-04-10 15:00:00+00:00", "end_timestamp": "2022-04-10 17:00:00+00:00", "participants": ["Liverpool", "Chelsea"]},
    {"event_id": "E002", "league": "La Liga", "sport": "Football", "country": "Spain", "begin_timestamp": "2022-04-10 20:00:00+02:00", "end_timestamp": "2022-04-10 22:00:00+02:00", "participants": ["Real Madrid", "Barcelona"]},
    {"event_id": "E003", "league": "Serie A", "sport": "Football", "country": "Italy", "begin_timestamp": "2022-04-12 21:00:00+02:00", "end_timestamp": "2022-04-12 23:00:00+02:00", "participants": ["Juventus", "AC Milan"]}
]

# Coupon data
coupons = [
{"coupon_id": "C001", "selections": [{"event_id": "E001", "odds": 2.0}], "stake": 10.0, "timestamp": "2022-04-08T09:30:00", "user_id": 1},
{"coupon_id": "C002", "selections": [{"event_id": "E002", "odds": 1.5}, {"event_id": "E003", "odds": 2.0}], "stake": 5.0, "timestamp": "2022-04-08T10:30:00", "user_id": 2},
{"coupon_id": "C003", "selections": [{"event_id": "E003", "odds": 2.5}], "stake": 20.0, "timestamp": "2022-04-08T11:30:00", "user_id": 3},
]

