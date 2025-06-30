from server.extensions import db, bcrypt  # ✅ import bcrypt instance from extensions

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')  # ✅ correct usage

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)  # ✅ correct usage

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }
