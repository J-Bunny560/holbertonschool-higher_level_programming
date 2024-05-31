#!/usr/bin/python3
#!/usr/bin/python3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Define the users dictionary at the top level
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}  # Initialize as an empty dictionary

@app.route("/")
def home():
    """Home page."""
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """Return user data."""
    user_list = [{"username": user, "user_data": users[user]} for user in users]
    return jsonify(user_list)

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
    if request.method == 'POST':
        data = request.get_json()
        if 'username' not in data:
            return jsonify({"error": "Username not provided"}), 400
        username = data["username"]
        if username in users:
            return jsonify({"error": f"User {username} already exists"}), 409
        users[username] = data
        return jsonify({"message": f"User {username} added successfully", "user_data": users[username]}), 201
    else:
        return jsonify({"error": "Invalid request method"}), 405

@app.route("/users")
def get_all_users():
    """Return all user data."""
    user_list = [{"username": user, "user_data": users[user]} for user in users]
    return jsonify(user_list)

if __name__ == "__main__":
    app.run(debug=True)
