from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from server.models.user import User
from server.extensions import db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# ✅ Register route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')  # ✅ Defaults to 'user' if not provided

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'✅ User registered successfully as {role}'}), 201

# ✅ Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    # ✅ Store in session
    session['user_id'] = user.id
    session['username'] = user.username
    session['role'] = user.role

    return jsonify({
        'message': f'✅ Logged in as {user.username}',
        'username': user.username,  # ✅ Needed for frontend greeting
        'role': user.role
    }), 200

# ✅ Logout route
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': '✅ Logged out successfully'}), 200

# ✅ Get current user session info
@auth_bp.route('/me', methods=['GET'])
def current_user():
    if 'username' not in session:
        return jsonify({'error': 'Not logged in'}), 401

    return jsonify({
        'username': session['username'],
        'role': session['role']
    }), 200
