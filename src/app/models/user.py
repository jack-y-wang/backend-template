from app import db

import bcrypt

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)

    # User info
    name = db.Column(db.String, nullable="False")
    username = db.Column(db.String, nullable="False", unique=True)
    email = db.Column(db.String, nullable="False")
    password_digest = db.Column(db.String, nullable=False)

    # Session informaiton
    sessions = db.relationship("Session", back_populates="user", cascade="all, delete")
    
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.username = kwargs.get("username")
        self.password_digest = bcrypt.hashpw(
            kwargs.get('password').encode('utf8'),
            bcrypt.gensalt(rounds=13)
        )
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode("utf8"), self.password_digest)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.username,
        }
