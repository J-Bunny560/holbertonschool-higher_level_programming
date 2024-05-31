#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root URL (“/”) and create a function to handle this route
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Define a route for the /data URL and create a function to handle this route
@app.route("/data")
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"name": "John", "age": 32, "city": "New York"}}
    user_list = [{"username": user, "user_data": users[user]} for user in users]
    return jsonify(user_list)

# Define a route for the /status URL and create a function to handle this route
@app.route("/status")
def status():
    return "OK"

# Define a route for the /users/<username> URL and create a function to handle this route
@app.route("/users/<username>")
def get_user(username):
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"name": "John", "age": 32, "city": "New York"}}
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

    # Define a route for the /add_user URL and create a function to handle this route

@app.route("/add_user", methods=["POST"])
def add_user():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"name": "John", "age": 32, "city": "New York"}}
    data = request.get_json()
    username = data["username"]
    users[username] = data
    return jsonify({"message": f"User {username} added successfully", "user_data": users[username]})


# Run the Flask development server
if __name__ == "__main__":
    app.run()
