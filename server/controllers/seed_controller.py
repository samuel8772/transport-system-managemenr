# server/controllers/seed_controller.py

from flask import Blueprint, jsonify
from server.extensions import db
from server.models.route import Route
from server.models.matatu import Matatu
from server.models.trip import Trip
from datetime import datetime, timedelta

seed_bp = Blueprint('seed', __name__, url_prefix='/api/seed')

@seed_bp.route('/trips', methods=['POST'])
def seed_trips():
    try:
        # Clear existing data
        Trip.query.delete()
        Matatu.query.delete()
        Route.query.delete()
        db.session.commit()

        # Create routes
        route1 = Route(origin="Nairobi", destination="Kisumu")
        route2 = Route(origin="Nairobi", destination="Mombasa")
        route3 = Route(origin="Eldoret", destination="Nakuru")

        # Create matatus
        matatu1 = Matatu(plate_number="KDA 123A", capacity=14)
        matatu2 = Matatu(plate_number="KDB 456B", capacity=11)
        matatu3 = Matatu(plate_number="KDC 789C", capacity=16)

        db.session.add_all([route1, route2, route3, matatu1, matatu2, matatu3])
        db.session.commit()

        # Create trips
        now = datetime.now()
        trip1 = Trip(route_id=route1.id, matatu_id=matatu1.id, date=now.date(), departure_time="09:00 AM", available_seats=matatu1.capacity)
        trip2 = Trip(route_id=route2.id, matatu_id=matatu2.id, date=now.date() + timedelta(days=1), departure_time="02:00 PM", available_seats=matatu2.capacity)
        trip3 = Trip(route_id=route3.id, matatu_id=matatu3.id, date=now.date() + timedelta(days=2), departure_time="07:00 AM", available_seats=matatu3.capacity)

        db.session.add_all([trip1, trip2, trip3])
        db.session.commit()

        return jsonify({"message": "✅ Seeded routes, matatus, and trips."}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
