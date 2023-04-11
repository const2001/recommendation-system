from datetime import datetime, timezone

# user_preferences = {
#     1: {"country": "Italy", "sport": "Football"},
#     2: {"country": "Germany", "sport": "Football"},
#     3: {"country": "Spain", "sport": "Football"}
# }

# Recommend coupons based on user preferences and odds


def recommend_coupons(user, coupons, events):

    recommended_coupons = []
    for coupon in coupons:
        coupon_odds = 1
        for selection in coupon["selections"]:
            event_id = selection["event_id"]
            event = next(
                (e for e in events if e["event_id"] == event_id), None)
            if event and event["country"] == user["country"] and event["sport"] == user["sport_pref"]:
                coupon_odds *= selection["odds"]
            else:
                coupon_odds = 0
                break
        if coupon_odds > 0:
            coupon_copy = coupon.copy()
            coupon_copy["odds"] = coupon_odds
            recommended_coupons.append(coupon_copy)
    return sorted(recommended_coupons, key=lambda x: x["odds"], reverse=True)


# User data
users = [
    {"user_id": 1, "birth_year": 1990, "country": "Italy", "sport_pref": "Football",
        "currency": "EUR", "registration_date": "2022-03-01T00:00:00", },
    {"user_id": 2, "birth_year": 1985, "country": "Germany", "sport_pref": "Football",
        "currency": "EUR", "registration_date": "2022-03-01T00:00:00"},
    {"user_id": 3, "birth_year": 1995, "country": "Spain", "sport_pref": "Football",
        "currency": "EUR", "registration_date": "2022-03-01T00:00:00"}
]

# Event data
events = [
    {"event_id": "E001", "league": "Premier League", "sport": "Football", "country": "England", "begin_timestamp":
        "2022-04-10 15:00:00+00:00", "end_timestamp": "2022-04-10 17:00:00+00:00", "participants": ["Liverpool", "Chelsea"]},
    {"event_id": "E002", "league": "La Liga", "sport": "Football", "country": "Spain", "begin_timestamp": "2022-04-10 20:00:00+02:00",
        "end_timestamp": "2022-04-10 22:00:00+02:00", "participants": ["Real Madrid", "Barcelona"]},
    {"event_id": "E003", "league": "Serie A", "sport": "Football", "country": "Italy", "begin_timestamp": "2022-04-12 21:00:00+02:00",
        "end_timestamp": "2022-04-12 23:00:00+02:00", "participants": ["Juventus", "AC Milan"]}
]

# Coupon data
coupons = [
    {"coupon_id": "C001", "selections": [{"event_id": "E001", "odds": 2.0}],
        "stake": 10.0, "timestamp": "2022-04-08T09:30:00", "user_id": 1},
    {"coupon_id": "C002", "selections": [{"event_id": "E002", "odds": 1.5}, {
        "event_id": "E003", "odds": 2.0}], "stake": 5.0, "timestamp": "2022-04-08T10:30:00", "user_id": 2},
    {"coupon_id": "C003", "selections": [{"event_id": "E003", "odds": 2.5}],
        "stake": 20.0, "timestamp": "2022-04-08T11:30:00", "user_id": 3},
]

# print(recommend_coupons(1, coupons, events)) # Outputs [{'coupon_id': 'C001', 'selections': [{'event_id': 'E001', 'odds': 2.0}], 'stake': 10.0, 'timestamp': '2022-04-08T09:30:00', 'user_id': 1, 'odds': 2.0}]
