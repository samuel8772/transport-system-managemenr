from server.extensions import db

class Route(db.Model):
    __tablename__ = 'routes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    origin = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(50), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    base_fare = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    trips = db.relationship('Trip', backref='route', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'origin': self.origin,
            'destination': self.destination,
            'distance': self.distance,
            'base_fare': self.base_fare,
            'duration': self.duration
        }
