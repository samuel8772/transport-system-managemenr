from flask import Blueprint, request, jsonify
from server.models.matatu import Matatu
from server.extensions import db

matatu_bp = Blueprint('matatus', __name__, url_prefix='/api/matatus')

@matatu_bp.route('/', methods=['GET'])
def get_matatus():
    matatus = Matatu.query.all()
    return jsonify([matatu.to_dict() for matatu in matatus]), 200

@matatu_bp.route('/', methods=['POST'])
def create_matatu():
    data = request.get_json()
    required_fields = ['registration_number', 'capacity', 'sacco_name', 'driver_name', 'conductor_name']
    if not all(k in data for k in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    if not isinstance(data['capacity'], int) or data['capacity'] <= 0:
        return jsonify({'error': 'Capacity must be a positive integer'}), 400

    existing = Matatu.query.filter_by(registration_number=data['registration_number']).first()
    if existing:
        return jsonify({'error': 'Registration number already exists'}), 400

    matatu = Matatu(
        registration_number=data['registration_number'],
        capacity=data['capacity'],
        sacco_name=data['sacco_name'],
        driver_name=data['driver_name'],
        conductor_name=data['conductor_name']
    )
    db.session.add(matatu)
    db.session.commit()

    return jsonify(matatu.to_dict()), 201
