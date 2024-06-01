from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Initialize an empty dictionary for users
users = {}

@app.route("/")
def home():
    """Home page."""
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """Return a list of all usernames and their info."""
    return jsonify(users)

@app.route("/users")
def list_users():
    """Return a list of all usernames."""
    user_list = list(users.keys())
    return jsonify(user_list)

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
    try:
        data = request.get_json()
        if not data or 'username' not in data:
            return jsonify({"error": "Username not provided"}), 400
        username = data["username"]
        if username in users:
            return jsonify({"error": f"User {username} already exists"}), 409
        users[username] = {
            "username": username,
            "name": data.get("name", ""),
            "age": data.get("age", 0),
            "city": data.get("city", "")
        }
        return jsonify({"message": "User added", "user": users[username]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
