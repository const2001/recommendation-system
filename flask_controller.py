from flask import Flask, request, jsonify
from validators import validate_user, validate_coupon, validate_event
from recommendation_gen import recommend_coupons
from DatabaseManager import addUserToDatabase,addEventToDatabase,addCouponToDatabase,getUsersFromDatabase,getCouponsFromDatabase,getEventsFromDatabase
from server_address import server_host,server_port


app = Flask(__name__)

users = getUsersFromDatabase()

events = getEventsFromDatabase()
# Coupon data
coupons = getCouponsFromDatabase()
# coupons = [
#     {
#         "coupon_id" : 1,
#         "selections": [{"event_id": 1, "odds": 2.0}],
#         "stake": 10.0,
#         "timestamp": "2022-04-08T09:30:00",
#         "user_id": 1,
#     },
#     {
#         "coupon_id" : 2,
#         "selections": [
#             {"event_id": 2, "odds": 1.5},
#             {"event_id": 3, "odds": 2.0},
#         ],
#         "stake": 5.0,
#         "timestamp": "2022-04-08T10:30:00",
#         "user_id": 2,
#     },
#     {
#         "coupon_id" : 3,
#         "selections": [{"event_id": 3, "odds": 2.5}],
#         "stake": 20.0,
#         "timestamp": "2022-04-08T11:30:00",
#         "user_id": 3,
#     },
#     {
#         "coupon_id" : 4,
#         "selections": [{"event_id": 3, "odds": 2.5}],
#         "stake": 20.0,
#         "timestamp": "2022-04-08T11:30:00",
#         "user_id": 3,
#     },
#     {
#         "coupon_id" : 5,
#         "selections": [{"event_id": 4, "odds": 1.8}],
#         "stake": 15.0,
#         "timestamp": "2022-04-13T09:30:00",
#         "user_id": 4,
#     },
#     {
#         "coupon_id" : 6,
#         "selections": [
#             {"event_id": 5, "odds": 1.5},
#             {"event_id": 6, "odds": 1.7},
#         ],
#         "stake": 10.0,
#         "timestamp": "2022-04-13T10:30:00",
#         "user_id": 5,
#     },
#     {
#         "coupon_id" : 7,
#         "selections": [{"event_id": 6, "odds": 2.3}],
#         "stake": 25.0,
#         "timestamp": "2022-04-13T11:30:00",
#         "user_id": 6,
#     },
# ]




def get_user_by_id(user_id):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return None

@app.route("/", methods=["GET"])
def get_info():
    return "Recommendation system server is up and running"

@app.route("/add_user", methods=["POST"])
def add_user():
    # Get the request data and validate it against the schema
    user_data = request.json
    user_data["user_id"] = len(users) + 1
    IsValid, Validation_result = validate_user(user_data)
    if IsValid:
        users.append(user_data)
        addUserToDatabase(user_data)
        return (
            jsonify(
                {
                    "message": "User added successfully",
                    "user": user_data,
                    "Result": Validation_result,
                }
            ),
            201,
        )

    return jsonify({"message": "Validation error", "Result": Validation_result}), 400


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


def add_event():
    # Get the request data and validate it against the schema
    event_data = request.json
    IsValid, Validation_result = validate_event(event_data)
    if IsValid:
        events.append(event_data)
        addEventToDatabase(event_data)
        return (
            jsonify(
                {
                    "message": "Event added successfully",
                    "user": event_data,
                    "Result": Validation_result,
                }
            ),
            201,
        )

    return jsonify({"message": "Validation error", "Result": Validation_result}), 400


@app.route("/events", methods=["GET"])
def get_events():
    
    return jsonify(events)


def add_coupon():
    # Get the request data and validate it against the schema
    coupon_data = request.json
    IsValid, Validation_result = validate_coupon(coupon_data)
    if IsValid:
        coupons.append(coupon_data)
        addCouponToDatabase(coupon_data)
        return (
            jsonify(
                {
                    "message": "Coupon added successfully",
                    "user": coupon_data,
                    "Result": Validation_result,
                }
            ),
            201,
        )

    return jsonify({"message": "Validation error", "Result": Validation_result}), 400


@app.route("/coupons", methods=["GET"])
def get_coupons():
    return jsonify(coupons)


@app.route("/recommendation", methods=["GET"])
def get_recommendation():
    user_id = request.args.get("user_id")
    if not user_id:
        return "No user ID provided", 400
    user = get_user_by_id(int(user_id))
    if user:
        rec_coupons = recommend_coupons(user, events, coupons)
    else:
        return "No user found"
    if rec_coupons:
        for rec_coupon in rec_coupons:
            IsValid, validationResult = validate_coupon(rec_coupon)
            if not IsValid:
                return (
                    jsonify({"message": "Validation error", "error": validationResult}),
                    400,
                )
        return jsonify({"recommended_coupons": rec_coupons})

    else:
        return "no coupons reccomended"


if __name__ == "__main__":    
    
    app.run(host=server_host(),port=server_port(),debug=True)
