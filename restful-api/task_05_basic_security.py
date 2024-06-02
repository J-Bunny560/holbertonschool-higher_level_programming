from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Replace with a more secure secret
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data (replace with database interaction in a real application)
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
    # Check if authentication was provided
    if not request.authorization:
        return jsonify({'message': 'Authentication required'}), 401

    # Authenticate the user
    auth.authenticate(auth=request.authorization)  # Pass auth argument
    user = auth.current_user

    # Create JWT token with user role
    access_token = create_access_token(identity=user['username'], fresh=True, additional_claims={"role": user['role']}) 
    return jsonify({'token': access_token}), 200

# Basic Authentication protected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify("Basic Auth: Access Granted"), 200

# JWT Authentication protected route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify("JWT Auth: Access Granted"), 200

# Role-based protected route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    # Get the user's role from the JWT token
    jwt_data = get_jwt()  # Get the entire JWT payload
    role = jwt_data['role']

    if role == "admin":
        return jsonify("Admin Access: Granted"), 200
    else:
        abort(403, "Unauthorized")

# Error handlers for JWT authentication failures
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)
