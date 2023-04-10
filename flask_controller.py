from flask import Flask, request, jsonify
from schema_classes import UserSchema,CouponSchema,EventSchema,ValidationError


app = Flask(__name__)

# Define an endpoint for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get the request data and validate it against the schema
    try:
        user_data = UserSchema().load(request.json)
    except ValidationError as error:
        return jsonify({'message': 'Validation error', 'errors': error.messages}), 400

    # Add the user to the database or perform any other required actions
    # ...

    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
