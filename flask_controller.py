from flask import Flask, request, jsonify
from validators import validate_user,validate_coupon,validate_event
from recommendation_gen import recommend_coupons


app = Flask(__name__)
# User data
users = [
    {
        "user_id": 1,
        "birth_year": 1990,
        "country": "Italy",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id": 2,
        "birth_year": 1985,
        "country": "Germany",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id": 3,
        "birth_year": 1995,
        "country": "Spain",
        "sport_pref": "Football",
        "currency": "EUR",
        "registration_date": "2022-03-01T00:00:00",
    },
    {
        "user_id": 4,
        "birth_year": 2000,
        "country": "France",
        "sport_pref": "Basketball",
        "currency": "EUR",
        "registration_date": "2022-04-10T00:00:00",
    },
    {
        "user_id": 5,
        "birth_year": 1998,
        "country": "USA",
        "sport_pref": "American Football",
        "currency": "USD",
        "registration_date": "2022-04-11T00:00:00",
    },
    {
        "user_id": 6,
        "birth_year": 1989,
        "country": "Brazil",
        "sport_pref": "Soccer",
        "currency": "BRL",
        "registration_date": "2022-04-12T00:00:00",
    },
]

# Event Data
events = [
    {
        "event_id": "E001",
        "league": "Premier League",
        "sport": "Football",
        "country": "England",
        "begin_timestamp": "2022-04-10 15:00:00+00:00",
        "end_timestamp": "2022-04-10 17:00:00+00:00",
        "participants": ["Liverpool", "Chelsea"],
    },
    {
        "event_id": "E002",
        "league": "La Liga",
        "sport": "Football",
        "country": "Spain",
        "begin_timestamp": "2022-04-10 20:00:00+02:00",
        "end_timestamp": "2022-04-10 22:00:00+02:00",
        "participants": ["Real Madrid", "Barcelona"],
    },
    {
        "event_id": "E003",
        "league": "Serie A",
        "sport": "Football",
        "country": "Italy",
        "begin_timestamp": "2022-04-12 21:00:00+02:00",
        "end_timestamp": "2022-04-12 23:00:00+02:00",
        "participants": ["Juventus", "AC Milan"],
    },
    {
        "event_id": "E056",
        "league": "Serie A",
        "sport": "Football",
        "country": "Italy",
        "begin_timestamp": "2022-04-12 21:00:00+02:00",
        "end_timestamp": "2022-04-12 23:00:00+02:00",
        "participants": ["Juventus", "AC Milan"],
    },
    {
        "event_id": "E004",
        "league": "NBA",
        "sport": "Basketball",
        "country": "USA",
        "begin_timestamp": "2022-04-14 19:00:00+00:00",
        "end_timestamp": "2022-04-14 21:00:00+00:00",
        "participants": ["Los Angeles Lakers", "Brooklyn Nets"],
    },
    {
        "event_id": "E005",
        "league": "NFL",
        "sport": "American Football",
        "country": "USA",
        "begin_timestamp": "2022-04-16 17:00:00+00:00",
        "end_timestamp": "2022-04-16 19:00:00+00:00",
        "participants": ["New England Patriots", "Tampa Bay Buccaneers"],
    },
    {
        "event_id": "E006",
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
        "coupon_id": "C001",
        "selections": [{"event_id": "E001", "odds": 2.0}],
        "stake": 10.0,
        "timestamp": "2022-04-08T09:30:00",
        "user_id": 1,
    },
    {
        "coupon_id": "C002",
        "selections": [
            {"event_id": "E002", "odds": 1.5},
            {"event_id": "E003", "odds": 2.0},
        ],
        "stake": 5.0,
        "timestamp": "2022-04-08T10:30:00",
        "user_id": 2,
    },
    {
        "coupon_id": "C003",
        "selections": [{"event_id": "E003", "odds": 2.5}],
        "stake": 20.0,
        "timestamp": "2022-04-08T11:30:00",
        "user_id": 3,
    },
    {
        "coupon_id": "C087",
        "selections": [{"event_id": "E003", "odds": 2.5}],
        "stake": 20.0,
        "timestamp": "2022-04-08T11:30:00",
        "user_id": 3,
    },
    {
        "coupon_id": "C004",
        "selections": [{"event_id": "E004", "odds": 1.8}],
        "stake": 15.0,
        "timestamp": "2022-04-13T09:30:00",
        "user_id": 4,
    },
    {
        "coupon_id": "C005",
        "selections": [
            {"event_id": "E005", "odds": 1.5},
            {"event_id": "E006", "odds": 1.7},
        ],
        "stake": 10.0,
        "timestamp": "2022-04-13T10:30:00",
        "user_id": 5,
    },
    {
        "coupon_id": "C006",
        "selections": [{"event_id": "E006", "odds": 2.3}],
        "stake": 25.0,
        "timestamp": "2022-04-13T11:30:00",
        "user_id": 6,
    },
]


def get_user_by_id(user_id):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None



@app.route("/add_user", methods=["POST"])
def add_user():
    # Get the request data and validate it against the schema
    user_data = request.json
    user_data["user_id"] =len(users)+1
    IsValid,Validation_result = validate_user(user_data)
    if(IsValid):
        users.append(user_data)
        return jsonify({"message": "User added successfully", "user": user_data,"Result": Validation_result}), 201
      
    return jsonify({"message": "Validation error", "Result": Validation_result}), 400

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# @app.route("/add_event", methods=["POST"])
# def add_user():
#     # Get the request data and validate it against the schema
#     try:
#         event_data = EventSchema().load(request.json)
#     except ValidationError as error:
#         return jsonify({"message": "Validation error", "errors": error.messages}), 400

#     users.append(event_data)
#     # Add the user to the database or perform any other required actions
#     # ...

#     return jsonify({"message": "User added successfully", "user": event_data}), 201

@app.route("/recommendation/", methods=["GET"])
def get_recommendation(user_id):
    user_id = request.args.get("user_id")
    if not user_id:
        return "No user ID provided",400
    if get_user_by_id(user_id):
        rec_coupons = recommend_coupons(
            get_user_by_id(user_id), coupons, events)
    else:
        return "No user found"
    if rec_coupons:
        try:
            schema = CouponSchema(many=True)
            result = schema.loads(rec_coupons)
            return jsonify({"recommended_coupons": result})
        except ValidationError as error:
            return (
                jsonify({"message": "Validation error",
                        "errors": error.messages}),
                400,
            )

    else:
        return "no coupons reccomended"


if __name__ == "__main__":
    app.run(debug=True)
