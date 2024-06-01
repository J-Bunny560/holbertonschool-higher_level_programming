from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Store users in a more secure way (e.g., a database)
users = {
    "jane": {"password": generate_password_hash("password123"), "role": "admin"},
    "john": {"password": generate_password_hash("password456"), "role": "user"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]
    return None

# Login route for obtaining JWT tokens
@app.route('/login', methods=['POST'])
def login():
    auth.authenticate()
    user = auth.current_user
    
    # Create a JWT token
    access_token = create_access_token(identity=user['username'])
    return jsonify({'token': access_token}), 200

# Protected route accessible with JWT token
@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(f'Hello, {current_user}!'), 200
