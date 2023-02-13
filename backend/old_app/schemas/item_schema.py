from marshmallow import Schema, fields, post_load
from old_app.models.item import Item


class ItemSchema(Schema):
    id = fields.Integer()
    description = fields.String(allow_none=False)
    category = fields.String()
    url = fields.String()
    vendor_id = fields.Integer(allow_none=False)
    date_created = fields.DateTime()
    last_updated = fields.DateTime()

    @post_load
    def make_item(self, data, **kwargs):
        return Item(**data)
