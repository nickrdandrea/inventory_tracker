from app import db


class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    category = db.Column(db.String)
    url = db.Column(db.String)
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())
    __table_args__ = (
        db.UniqueConstraint(
            "description", "vendor_id", name="_description_vendor_id_uc"
        ),
    )

    def __repr__(self):
        return (
            "Item ("
            f"id={self.id!r}, "
            f"description={self.description!r}, "
            f"category={self.category!r}, "
            f"last_updated={self.last_updated!r})"
        )
