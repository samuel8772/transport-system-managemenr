from server.extensions import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passengers.id'), nullable=False)
    seat_number = db.Column(db.Integer, nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)
    fare_paid = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), default='pending')

    # Relationships
    trip = db.relationship("Trip", back_populates="bookings")
    passenger = db.relationship("Passenger", back_populates="bookings")

    def __init__(self, trip_id, passenger_id, seat_number, fare_paid, payment_status='pending'):
        self.trip_id = trip_id
        self.passenger_id = passenger_id
        self.seat_number = seat_number
        self.fare_paid = fare_paid
        self.payment_status = payment_status

    def to_dict(self):
        return {
            'id': self.id,
            'trip_id': self.trip_id,
            'passenger_id': self.passenger_id,
            'seat_number': self.seat_number,
            'booking_time': self.booking_time.isoformat(),
            'fare_paid': self.fare_paid,
            'payment_status': self.payment_status,
            'trip': self.trip.to_dict() if self.trip else None,
            'passenger': self.passenger.to_dict() if self.passenger else None
        }
