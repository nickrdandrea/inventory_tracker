from werkzeug.security import generate_password_hash, check_password_hash

from old_app import db
from old_app import jwt
from old_app.models import Item

watched_items = db.Table('watched_items', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))

    alerts = db.relationship("Alert", backref="user")
    watched_items = db.relationship(
        'Item', secondary=watched_items,
        primaryjoin=(watched_items.c.user_id == id),
        secondaryjoin=(watched_items.c.item_id == Item.id),
        backref=db.backref('watched_items', lazy='dynamic'), lazy='dynamic'
    )
    
    def __repr__(self):
        return "User (" f"id={self.id!r}, " f"name={self.name!r})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()