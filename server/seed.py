from datetime import datetime, timedelta
from server.app import app
from server.extensions import db
from server.models.user import User
from server.models.matatu import Matatu
from server.models.route import Route
from server.models.trip import Trip
from server.models.booking import Booking
from server.models.passenger import Passenger  # ✅ required for booking
from werkzeug.security import generate_password_hash

with app.app_context():
    print("🌱 Seeding data...")

    # Clear existing data
    Booking.query.delete()
    Trip.query.delete()
    Matatu.query.delete()
    Route.query.delete()
    Passenger.query.delete()
    User.query.delete()

    # Users
    user1 = User(
        username="sam",
        email="sam@example.com",
        password_hash=generate_password_hash("password"),
        role="admin"
    )
    user2 = User(
        username="jane",
        email="jane@example.com",
        password_hash=generate_password_hash("password123"),
        role="user"
    )
    db.session.add_all([user1, user2])
    db.session.commit()

    # Passengers (linked to user manually if needed)
    passenger1 = Passenger(name="Jane Doe", phone_number="0700111222", email="jane@example.com")
    passenger2 = Passenger(name="Mike Otieno", phone_number="0712345678", email="mike@example.com")
    db.session.add_all([passenger1, passenger2])
    db.session.commit()

    # Matatus
    matatus = [
        Matatu(
            registration_number="KDA123A", capacity=14,
            sacco_name="Super Metro", driver_name="John Doe", conductor_name="Ali Hassan"
        ),
        Matatu(
            registration_number="KDB456B", capacity=33,
            sacco_name="Transline", driver_name="Jane Muthoni", conductor_name="Peter Kariuki"
        ),
        Matatu(
            registration_number="KDC789C", capacity=14,
            sacco_name="Mololine", driver_name="Joseph Kamau", conductor_name="Samuel Otieno"
        ),
    ]
    db.session.add_all(matatus)

    # Routes
    routes = [
        Route(name="Nairobi - Nakuru", origin="Nairobi", destination="Nakuru", distance=160.0, base_fare=600.0, duration=3),
        Route(name="Nairobi - Kisumu", origin="Nairobi", destination="Kisumu", distance=350.0, base_fare=1200.0, duration=6),
        Route(name="Nairobi - Mombasa", origin="Nairobi", destination="Mombasa", distance=490.0, base_fare=1500.0, duration=8),
        Route(name="Nairobi - Eldoret", origin="Nairobi", destination="Eldoret", distance=310.0, base_fare=1000.0, duration=5),
        Route(name="Nairobi - Meru", origin="Nairobi", destination="Meru", distance=270.0, base_fare=800.0, duration=4),
    ]
    db.session.add_all(routes)
    db.session.commit()

    # Trips
    departure1 = datetime.strptime("2025-07-02 08:00:00", "%Y-%m-%d %H:%M:%S")
    departure2 = datetime.strptime("2025-07-02 09:30:00", "%Y-%m-%d %H:%M:%S")
    departure3 = datetime.strptime("2025-07-03 07:15:00", "%Y-%m-%d %H:%M:%S")

    trip1 = Trip(
        route_id=routes[0].id,
        matatu_id=matatus[0].id,
        departure_time=departure1,
        arrival_time=departure1 + timedelta(hours=routes[0].duration),
        available_seats=14
    )
    trip2 = Trip(
        route_id=routes[1].id,
        matatu_id=matatus[1].id,
        departure_time=departure2,
        arrival_time=departure2 + timedelta(hours=routes[1].duration),
        available_seats=33
    )
    trip3 = Trip(
        route_id=routes[2].id,
        matatu_id=matatus[2].id,
        departure_time=departure3,
        arrival_time=departure3 + timedelta(hours=routes[2].duration),
        available_seats=14
    )

    db.session.add_all([trip1, trip2, trip3])
    db.session.commit()

    # Bookings (using passenger_id, seat_number, fare_paid)
    booking1 = Booking(
        trip_id=trip1.id,
        passenger_id=passenger1.id,
        seat_number=1,
        fare_paid=routes[0].base_fare
    )
    booking2 = Booking(
        trip_id=trip2.id,
        passenger_id=passenger2.id,
        seat_number=2,
        fare_paid=routes[1].base_fare
    )

    db.session.add_all([booking1, booking2])
    db.session.commit()

    print("✅ Done seeding!")
