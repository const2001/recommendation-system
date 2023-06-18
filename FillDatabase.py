from DatabaseManager import addCouponToDatabase,addEventToDatabase,addUserToDatabase

# User data
users = [
    {
        "user_id" : 1,
        "birth_year": 1990,
        "gender": "Male",
        "country": "Italy",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id" : 2,
        "birth_year": 1985,
        "gender": "Male",
        "country": "Germany",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id" : 3,
        "birth_year": 1995,
        "gender": "Male",
        "country": "Spain",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id" : 4,
        "birth_year": 2000,
        "gender": "Male",
        "country": "France",
        "sport_pref": "Basketball",
        "currency": "EUR",
        "registration_date": "2022-04-10T00:00:00",
    },
    {
        "user_id" : 5,
        "birth_year": 1998,
        "gender": "Male",
        "country": "USA",
        "sport_pref": "American Football",
        "currency": "USD",
        "registration_date": "2022-04-11T00:00:00",
    },
    {
        "user_id" : 6,
        "birth_year": 1989,
        "gender": "Male",
        "country": "Brazil",
        "sport_pref": "Soccer",
        "currency": "BRL",
        "registration_date": "2022-04-12T00:00:00",
    },
]

# Event Data
events = [
    {
        "event_id" :1,
        "league": "Premier League",
        "sport": "Football",
        "country": "England",
        "begin_timestamp": "2022-04-10 15:00:00+00:00",
        "end_timestamp": "2022-04-10 17:00:00+00:00",
        "participants": ["Liverpool", "Chelsea"],
    },
    {
        "event_id" :2,
        "league": "La Liga",
        "sport": "Football",
        "country": "Spain",
        "begin_timestamp": "2022-04-10 20:00:00+02:00",
        "end_timestamp": "2022-04-10 22:00:00+02:00",
        "participants": ["Real Madrid", "Barcelona"],
    },
    {
        "event_id" :3,
        "league": "Serie A",
        "sport": "Football",
        "country": "Italy",
        "begin_timestamp": "2022-04-12 21:00:00+02:00",
        "end_timestamp": "2022-04-12 23:00:00+02:00",
        "participants": ["Juventus", "AC Milan"],
    },
    {
        "event_id" :4,
        "league": "Serie A",
        "sport": "Football",
        "country": "Italy",
        "begin_timestamp": "2022-04-12 21:00:00+02:00",
        "end_timestamp": "2022-04-12 23:00:00+02:00",
        "participants": ["Juventus", "AC Milan"],
    },
    {
        "event_id" :5,
        "league": "NBA",
        "sport": "Basketball",
        "country": "USA",
        "begin_timestamp": "2022-04-14 19:00:00+00:00",
        "end_timestamp": "2022-04-14 21:00:00+00:00",
        "participants": ["Los Angeles Lakers", "Brooklyn Nets"],
    },
    {
        "event_id" :6,
        "league": "NFL",
        "sport": "American Football",
        "country": "USA",
        "begin_timestamp": "2022-04-16 17:00:00+00:00",
        "end_timestamp": "2022-04-16 19:00:00+00:00",
        "participants": ["New England Patriots", "Tampa Bay Buccaneers"],
    },
    {
        "event_id" :7,
        "league": "Copa Libertadores",
        "sport": "Soccer",
        "country": "Brazil",
        "begin_timestamp": "2022-04-20 20:00:00-03:00",
        "end_timestamp": "2022-04-20 22:00:00-03:00",
        "participants": ["Santos FC", "Palmeiras"],
    },
]

# Coupon data
coupons = [
    {
        "coupon_id" : 1,
        "selections": [{"event_id": 1, "odds": 2.0}],
        "stake": 10.0,
        "timestamp": "2022-04-08T09:30:00",
        "user_id": 1,
    },
    {
        "coupon_id" : 2,
        "selections": [
            {"event_id": 2, "odds": 1.5},
            {"event_id": 3, "odds": 2.0},
        ],
        "stake": 5.0,
        "timestamp": "2022-04-08T10:30:00",
        "user_id": 2,
    },
    {
        "coupon_id" : 3,
        "selections": [{"event_id": 3, "odds": 2.5}],
        "stake": 20.0,
        "timestamp": "2022-04-08T11:30:00",
        "user_id": 3,
    },
    {
        "coupon_id" : 4,
        "selections": [{"event_id": 3, "odds": 2.5}],
        "stake": 20.0,
        "timestamp": "2022-04-08T11:30:00",
        "user_id": 3,
    },
    {
        "coupon_id" : 5,
        "selections": [{"event_id": 4, "odds": 1.8}],
        "stake": 15.0,
        "timestamp": "2022-04-13T09:30:00",
        "user_id": 4,
    },
    {
        "coupon_id" : 6,
        "selections": [
            {"event_id": 5, "odds": 1.5},
            {"event_id": 6, "odds": 1.7},
        ],
        "stake": 10.0,
        "timestamp": "2022-04-13T10:30:00",
        "user_id": 5,
    },
    {
        "coupon_id" : 7,
        "selections": [{"event_id": 6, "odds": 2.3}],
        "stake": 25.0,
        "timestamp": "2022-04-13T11:30:00",
        "user_id": 6,
    },
]
def getDummyUsers():
    return users

def getDummyEvents():
    return events

def getDummyCoupons():
    return coupons

# for user in users:
#     addUserToDatabase(user)
for event in events:
    addEventToDatabase(event)    
 
for coupon in coupons:
     addCouponToDatabase(coupon)