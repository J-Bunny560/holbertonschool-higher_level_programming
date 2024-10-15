#!/usr/bin/python3
""" This module contains the Flask app """
from flask import Flask, jsonify, request
app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}



@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    return jsonify(list(users.values()))

@app.route("/status")
def get_status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = data
    return jsonify(data), 201

if __name__ == "__main__":
    app.run()
