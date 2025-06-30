from flask import Blueprint, request, jsonify
from server.models.trip import Trip
from server.extensions import db

trip_bp = Blueprint('trips', __name__, url_prefix='/api/trips')

@trip_bp.route('/', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    return jsonify([trip.to_dict() for trip in trips]), 200

@trip_bp.route('/<int:id>', methods=['GET'])
def get_trip(id):
    trip = Trip.query.get(id)
    if not trip:
        return jsonify({'error': 'Trip not found'}), 404
    return jsonify(trip.to_dict()), 200

@trip_bp.route('/', methods=['POST'])
def create_trip():
    data = request.get_json()
    required_fields = ['route_id', 'matatu_id', 'departure_time', 'arrival_time', 'available_seats']
    if not all(k in data for k in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        trip = Trip(
            route_id=data['route_id'],
            matatu_id=data['matatu_id'],
            departure_time=data['departure_time'],
            arrival_time=data['arrival_time'],
            available_seats=data['available_seats']
        )
        db.session.add(trip)
        db.session.commit()
        return jsonify(trip.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@trip_bp.route('/<int:id>', methods=['PATCH'])
def update_trip(id):
    trip = Trip.query.get(id)
    if not trip:
        return jsonify({'error': 'Trip not found'}), 404

    data = request.get_json()
    try:
        for key in ['route_id', 'matatu_id', 'departure_time', 'arrival_time', 'available_seats']:
            if key in data:
                setattr(trip, key, data[key])
        db.session.commit()
        return jsonify(trip.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@trip_bp.route('/<int:id>', methods=['DELETE'])
def delete_trip(id):
    trip = Trip.query.get(id)
    if not trip:
        return jsonify({'error': 'Trip not found'}), 404

    try:
        db.session.delete(trip)
        db.session.commit()
        return jsonify({'message': 'Trip deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
