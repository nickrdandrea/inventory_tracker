from app.db import db


class Vendor(db.Model):
    __tablename__ = "vendor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())
    __table_args__ = (db.UniqueConstraint("name", name="_vendor_name_uc"),)

    items = db.relationship("Item", backref="vendor")

    def __repr__(self):
        return (
            "Vendor ("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"date_created={self.date_created!r},"
            f"last_updated={self.last_updated!r})"
        )
