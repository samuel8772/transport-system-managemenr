# server/utils.py

import re
from datetime import datetime, timedelta
from functools import wraps
from flask import jsonify, session
from server.extensions import db
from server.models.route import Route
from server.models.matatu import Matatu
from server.models.passenger import Passenger
from server.models.trip import Trip
from server.models.booking import Booking

def validate_kenyan_phone(phone):
    pattern = r'^(\+254|0)[7][0-9]{8}$'
    return re.match(pattern, phone) is not None

def validate_email(email):
    if not email:
        return True
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def init_sample_data(app):
    with app.app_context():
        db.create_all()
        if Route.query.first():
            return

        routes = [
            Route(name="Nairobi-Mombasa Highway", origin="Nairobi", destination="Mombasa", distance=483, base_fare=1500, duration=480),
            Route(name="Nairobi-Kisumu", origin="Nairobi", destination="Kisumu", distance=350, base_fare=1200, duration=360),
            Route(name="Nairobi-Eldoret", origin="Nairobi", destination="Eldoret", distance=312, base_fare=1000, duration=300),
            Route(name="Nairobi-Nakuru", origin="Nairobi", destination="Nakuru", distance=160, base_fare=500, duration=180),
            Route(name="Mombasa-Malindi", origin="Mombasa", destination="Malindi", distance=120, base_fare=400, duration=120)
        ]
        matatus = [
            Matatu(registration_number="KCA123A", capacity=14, sacco_name="Nairobi Shuttle", driver_name="John Kiprotich", conductor_name="Mary Wanjiku"),
            Matatu(registration_number="KCB456B", capacity=14, sacco_name="Coast Express", driver_name="Hassan Omar", conductor_name="Grace Muthoni"),
            Matatu(registration_number="KCC789C", capacity=18, sacco_name="Western Line", driver_name="Peter Ochieng", conductor_name="Janet Akinyi"),
            Matatu(registration_number="KCD012D", capacity=14, sacco_name="Rift Valley Express", driver_name="Samuel Kiptoo", conductor_name="Rose Chebet"),
            Matatu(registration_number="KCE345E", capacity=11, sacco_name="Malindi Express", driver_name="Ali Abdalla", conductor_name="Fatuma Said")
        ]
        passengers = [
            Passenger(name="James Mwangi", phone_number="0712345678", email="james@email.com"),
            Passenger(name="Aisha Mohamed", phone_number="0723456789", email="aisha@email.com"),
            Passenger(name="David Kiprotich", phone_number="0734567890", email="david@email.com")
        ]
        db.session.add_all(routes + matatus + passengers)
        db.session.commit()

        base_time = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)
        trips = [
            Trip(
                route_id=1,
                matatu_id=1,
                departure_time=base_time,
                arrival_time=base_time + timedelta(minutes=routes[0].duration),
                available_seats=matatus[0].capacity,
                status="scheduled"
            ),
            Trip(
                route_id=2,
                matatu_id=2,
                departure_time=base_time + timedelta(hours=2),
                arrival_time=base_time + timedelta(hours=2, minutes=routes[1].duration),
                available_seats=matatus[1].capacity,
                status="scheduled"
            ),
            Trip(
                route_id=3,
                matatu_id=3,
                departure_time=base_time + timedelta(hours=4),
                arrival_time=base_time + timedelta(hours=4, minutes=routes[2].duration),
                available_seats=matatus[2].capacity,
                status="scheduled"
            )
        ]
        db.session.add_all(trips)
        db.session.commit()

# Role-based access control decorator
def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            role = session.get("role")
            if role != required_role:
                return jsonify({"error": "Access forbidden: insufficient role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
