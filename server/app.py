from flask import Flask
from server.config import Config
from server.extensions import db, migrate, cors, bcrypt
from server.models import *
from server.controllers import register_routes
from server.utils import validate_kenyan_phone, validate_email, init_sample_data

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.secret_key = 'super-secret-session-key'

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    bcrypt.init_app(app)

    register_routes(app)

    @app.route('/')
    def index():
        return {"message": "Matatu System API is running."}

    @app.route('/api/test')
    def test():
        return {"message": "✅ Hello from Flask backend!"}

    return app

# ✅ Expose app globally
app = create_app()

if __name__ == '__main__':
    init_sample_data(app)
    app.run(debug=True)
