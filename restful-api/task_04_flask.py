#!/usr/bin/python3
""" This module contains the Flask app """
from flask import Flask, jsonify, request
app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}



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
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added successfully"})

if __name__ == "__main__":
    app.run()
