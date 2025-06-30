# server/controllers/register_routes.py

from .auth_controller import auth_bp
from .route_controller import route_bp
from .matatu_controller import matatu_bp
from .passenger_controller import passenger_bp
from .trip_controller import trip_bp
from .booking_controller import booking_bp
from .seed_controller import seed_bp  # ✅ Import new seed controller

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(route_bp, url_prefix='/api/routes')
    app.register_blueprint(matatu_bp, url_prefix='/api/matatus')
    app.register_blueprint(passenger_bp, url_prefix='/api/passengers')
    app.register_blueprint(trip_bp, url_prefix='/api/trips')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(seed_bp, url_prefix='/api/seed')  # ✅ Register seed routes
