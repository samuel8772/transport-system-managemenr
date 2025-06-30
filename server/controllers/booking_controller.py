# server/controllers/booking_controller.py

from flask import Blueprint, request, jsonify, session
from server.models.booking import Booking
from server.models.trip import Trip
from server.models.passenger import Passenger
from server.extensions import db

booking_bp = Blueprint('bookings', __name__, url_prefix='/api/bookings')

# 🔍 GET all bookings for the current user
@booking_bp.route('/', methods=['GET'])
def get_bookings():
    passenger_id = session.get('user_id')
    if not passenger_id:
        return jsonify({"error": "Unauthorized"}), 401

    bookings = Booking.query.filter_by(passenger_id=passenger_id).all()
    return jsonify([b.to_dict() for b in bookings]), 200

# 🔍 GET single booking by ID
@booking_bp.route('/<int:id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get_or_404(id)
    return jsonify(booking.to_dict()), 200

# ➕ POST create booking
@booking_bp.route('/', methods=['POST'])
def create_booking():
    data = request.get_json()
    trip_id = data.get('trip_id')
    seat_number = data.get('seat_number')
    passenger_id = session.get('user_id')

    if not passenger_id:
        return jsonify({"error": "Unauthorized"}), 401
    if not all([trip_id, seat_number]):
        return jsonify({"error": "trip_id and seat_number are required"}), 400

    trip = Trip.query.get(trip_id)
    passenger = Passenger.query.get(passenger_id)

    if not trip:
        return jsonify({"error": "Trip not found"}), 404
    if not passenger:
        return jsonify({"error": "Passenger not found"}), 404
    if trip.available_seats < 1:
        return jsonify({"error": "No seats available on this trip"}), 400

    booking = Booking(trip_id=trip_id, passenger_id=passenger_id, seat_number=seat_number)
    trip.available_seats -= 1

    db.session.add(booking)
    db.session.commit()
    return jsonify(booking.to_dict()), 201

# 🛠 PATCH update booking
@booking_bp.route('/<int:id>', methods=['PATCH'])
def update_booking(id):
    booking = Booking.query.get_or_404(id)
    data = request.get_json()
    booking.seat_number = data.get('seat_number', booking.seat_number)
    db.session.commit()
    return jsonify(booking.to_dict()), 200

# ❌ DELETE booking
@booking_bp.route('/<int:id>', methods=['DELETE'])
def delete_booking(id):
    booking = Booking.query.get_or_404(id)
    trip = Trip.query.get(booking.trip_id)
    if trip:
        trip.available_seats += 1
    db.session.delete(booking)
    db.session.commit()
    return jsonify({"message": "Booking deleted"}), 200

# 🧪 POST /api/bookings/seed – Seed sample booking
@booking_bp.route('/seed', methods=['POST'])
def seed_booking():
    passenger_id = session.get('user_id')
    trip = Trip.query.first()

    if not trip or not passenger_id:
        return jsonify({"error": "Trip or session user not found."}), 400

    new_booking = Booking(
        trip_id=trip.id,
        passenger_id=passenger_id,
        seat_number=1
    )
    trip.available_seats -= 1
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Test booking created ✅"}), 201
