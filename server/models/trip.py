from server.extensions import db

class Trip(db.Model):
    __tablename__ = 'trips'
    
    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'), nullable=False)
    matatu_id = db.Column(db.Integer, db.ForeignKey('matatus.id'), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='scheduled')

    # Relationship to Booking
    bookings = db.relationship(
        'Booking',
        back_populates='trip',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __init__(self, route_id, matatu_id, departure_time, arrival_time, available_seats, status='scheduled'):
        self.route_id = route_id
        self.matatu_id = matatu_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.available_seats = available_seats
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'route_id': self.route_id,
            'matatu_id': self.matatu_id,
            'departure_time': self.departure_time.isoformat(),
            'arrival_time': self.arrival_time.isoformat(),
            'available_seats': self.available_seats,
            'status': self.status,
            'route': self.route.to_dict() if hasattr(self, 'route') else None,
            'matatu': self.matatu.to_dict() if hasattr(self, 'matatu') else None
        }
