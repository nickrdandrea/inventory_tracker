from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import db


class User(UserMixin,db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))

    alerts = db.relationship("Alert", backref="user")

    def __repr__(self):
        return "User (" f"id={self.id!r}, " f"name={self.name!r})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
