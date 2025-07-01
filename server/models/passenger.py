from server.extensions import db

class Passenger(db.Model):
    __tablename__ = 'passengers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    
    bookings = db.relationship(
        'Booking',
        back_populates='passenger',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __init__(self, name, phone_number, email=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email
        }
