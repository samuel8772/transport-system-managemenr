import re
from flask import Blueprint, request, jsonify
from server.models.passenger import Passenger
from server.extensions import db

passenger_bp = Blueprint('passengers', __name__, url_prefix='/api/passengers')

def validate_kenyan_phone(phone):
    pattern = r'^(\+254|0)[7][0-9]{8}$'
    return re.match(pattern, phone) is not None

def validate_email(email):
    if not email:
        return True
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@passenger_bp.route('/', methods=['GET'])
def get_passengers():
    passengers = Passenger.query.all()
    return jsonify([passenger.to_dict() for passenger in passengers]), 200

@passenger_bp.route('/', methods=['POST'])
def create_passenger():
    data = request.get_json()
    if not all(k in data for k in ['name', 'phone_number']):
        return jsonify({'error': 'Name and phone number are required'}), 400

    if not validate_kenyan_phone(data['phone_number']):
        return jsonify({'error': 'Invalid Kenyan phone number format'}), 400

    if data.get('email') and not validate_email(data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    passenger = Passenger(
        name=data['name'],
        phone_number=data['phone_number'],
        email=data.get('email')
    )
    db.session.add(passenger)
    db.session.commit()

    return jsonify(passenger.to_dict()), 201
