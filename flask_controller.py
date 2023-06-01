from flask import Flask, request, jsonify
from validators import validate_user, validate_coupon, validate_event
from recommendation_gen import recommend_coupons
from DatabaseManager import addUserToDatabase,addEventToDatabase,addCouponToDatabase,getUsersFromDatabase,getCouponsFromDatabase,getEventsFromDatabase,DatabaseConnection
from server_address import server_host,server_port


app = Flask(__name__)



def get_user_by_id(user_id):
    conn = DatabaseConnection().get_connection()
    users = getUsersFromDatabase(conn)
    conn.close()
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
    conn = DatabaseConnection().get_connection()
    users = getUsersFromDatabase(conn)
    
    user_data = request.json
    user_data["user_id"] = len(users) + 1
    IsValid, Validation_result = validate_user(user_data)
    if IsValid:
        users.append(user_data)
        addUserToDatabase(user_data,conn)
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
    conn.close()
    return jsonify({"message": "Validation error", "Result": Validation_result}), 400


@app.route("/users", methods=["GET"])
def get_users():
    conn = DatabaseConnection().get_connection()
    users = getUsersFromDatabase(conn)
    conn.close()
    return jsonify(users)


def add_event():
    # Get the request data and validate it against the schema
    event_data = request.json
    IsValid, Validation_result = validate_event(event_data)

    if IsValid:
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
    conn = DatabaseConnection().get_connection()
    events = getEventsFromDatabase(conn)
    conn.close()
    return jsonify(events)


def add_coupon():
    # Get the request data and validate it against the schema
    coupon_data = request.json
    conn = DatabaseConnection().get_connection()
    IsValid, Validation_result = validate_coupon(coupon_data)
    if IsValid:
        addCouponToDatabase(coupon_data,conn)
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
    conn.close()
    return jsonify({"message": "Validation error", "Result": Validation_result}), 400


@app.route("/coupons", methods=["GET"])
def get_coupons():
    conn = DatabaseConnection().get_connection()
    coupons = getCouponsFromDatabase(conn)
    conn.close()
    return jsonify(coupons)


@app.route("/recommendation", methods=["GET"])
def get_recommendation():
    conn = DatabaseConnection().get_connection()
    events = getEventsFromDatabase(conn)
    coupons = getCouponsFromDatabase(conn)
    conn.close()
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
