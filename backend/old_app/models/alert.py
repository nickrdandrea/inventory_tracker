from old_app import db


class Alert(db.Model):
    __tablename__ = "alert"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    category = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return (
            "Alert ("
            f"id={self.id!r}, "
            f"description={self.description!r}, "
            f"category={self.category!r}, "
            f"last_updated={self.last_updated!r})"
        )
