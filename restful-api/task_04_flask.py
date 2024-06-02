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
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    if not request.is_json:
        return jsonify({"error": "Invalid request"}), 400

    data = request.json
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
