from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Initialize an empty dictionary for users
users = {}

@app.route("/")
def home():
    """Home page."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Return a list of all usernames."""
    if not users:
        abort(404, description="No users found")
        return jsonify(list(users.keys()))


@app.route("/users")
def list_users():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """Return the API status."""
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Return user data for a given username."""
    if username not in users:
        abort(404, description="User not found")
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    if not request.is_json:
        abort(400, description="Request must be JSON")

    data = request.get_json()
    if not data or 'username' not in data:
        abort(400, description="Username not provided")
    username = data["username"]

    if username in users:
        abort(409, description=f"User {username} already exists")

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
