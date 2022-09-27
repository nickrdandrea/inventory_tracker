from unicodedata import name
from marshmallow import Schema, fields, post_load
from app.models.vendor import Vendor


class VendorSchema(Schema):

    id = fields.Integer()
    name = fields.String(allow_none=False)
    url = fields.String()
    date_created = fields.DateTime()
    last_updated = fields.DateTime()

    @post_load
    def make_item(self, data, **kwargs):
        return Vendor(**data)
