from server.extensions import db

class Matatu(db.Model):
    __tablename__ = 'matatus'
    
    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(10), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    sacco_name = db.Column(db.String(100), nullable=False)
    driver_name = db.Column(db.String(100), nullable=False)
    conductor_name = db.Column(db.String(100), nullable=False)
    
    trips = db.relationship('Trip', backref='matatu', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'registration_number': self.registration_number,
            'capacity': self.capacity,
            'sacco_name': self.sacco_name,
            'driver_name': self.driver_name,
            'conductor_name': self.conductor_name
        }
