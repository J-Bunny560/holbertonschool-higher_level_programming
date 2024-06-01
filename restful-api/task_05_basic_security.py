from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "jane": {"password": generate_password_hash("password123"), "role": "admin"},
    "john": {"password": generate_password_hash("password456"), "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]
    return None

@app.route("/")
@auth.login_required
def home():
    """Home page."""
    return "Welcome to the Flask API!"

@app.route("/data")
@auth.login_required
def data():
    """Return a list of all usernames and their info."""
    return jsonify(users)

@app.route("/users")
@auth.login_required
def list_users():
    """Return a list of all usernames."""
    user_list = list(users.keys())
    return jsonify(user_list)

@app.route("/status")
@auth.login_required
def status():
    """Return the API status."""
    return "OK"

@app.route("/users/<username>")
@auth.login_required
def get_user(username):
    """Return user data for a given username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
@auth.login_required
def add_user():
    """Add a new user."""
    try:
        data = request.get_json()
        if not data or 'username' not in data:
            return jsonify({"error": "Username not provided"}), 400
        username = data["username"]
        if username in users:
            return jsonify({"error": f"User {username} already exists"}), 409
        users[username] = {
            "username": username,
            "password": generate_password_hash(data["password"]),
            "role": data.get("role", "user")
        }
        return jsonify({"message": "User added", "user": users[username]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
