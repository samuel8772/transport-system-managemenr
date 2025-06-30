from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt  # ✅ Add this

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
bcrypt = Bcrypt()  # ✅ Initialize bcrypt
