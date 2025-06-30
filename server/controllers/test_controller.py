# server/controllers/test_controller.py

from flask import Blueprint, jsonify, session
from server.utils import role_required

test_bp = Blueprint('test', __name__, url_prefix='/api/test')

# ✅ Base route to confirm backend connection
@test_bp.route('/')
def test_home():
    return jsonify({"message": "✅ Backend connected!"}), 200

# ✅ Admin-only test route
@test_bp.route('/admin-only')
@role_required('admin')
def admin_only_view():
    return jsonify({"message": "Welcome, Admin! 🎉"}), 200

# ✅ User-only test route
@test_bp.route('/user-only')
@role_required('user')
def user_only_view():
    return jsonify({"message": "Welcome, User! 👋"}), 200

# ✅ Session info route
@test_bp.route('/whoami')
def whoami():
    return jsonify({
        "username": session.get("username"),
        "role": session.get("role")
    }), 200
