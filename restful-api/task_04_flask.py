#!/usr/bin/python3
import http.server
import json

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes('Hello, this is a simple API!', "utf-8"))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(data), "utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('OK', "utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf-8"))
        else:
            # Send 404 Not Found response for any other path
            self.send_error(404, "File Not Found: %s" % self.path)

def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """
    Home route that returns a welcome message.
    """
    return "Welcome to the Flask API!"

# Dictionary to store all users
users = {}

@app.route("/data")
def data():
    """
    Data route that returns all users.
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
    The new user's data is expected to be provided in the request body as JSON.
    """
    new_user = request.get_json()
    if not new_user:
        return jsonify({"error": "Missing JSON data"}), 400

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
