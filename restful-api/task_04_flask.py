#!/usr/bin/python3
""" This module contains the Flask app """
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"

users ={}

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added successfully", "users": new_user})

if __name__ == "__main__":
    app.run()
