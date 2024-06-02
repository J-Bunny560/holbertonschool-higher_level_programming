from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route that returns a welcome.
    """
    return "Welcome to the Flask API!"

# Dictionary to store all users
users = {}

@app.route("/data")
def data():
    """
    Data route that returns users.
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    """
    Status route that returns 'OK'.
    """
    return "OK"

@app.route("/users/<username>")
def user(username):
    """
    User route that returns the user with the given username.
    If the user does not exist, it returns a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add User route that accepts POST requests to add a new user.
    The new user's data is JSON.
    """
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username == users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
