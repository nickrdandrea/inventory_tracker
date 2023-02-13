from marshmallow import Schema, fields, post_load
from old_app.models.alert import Alert


class AlertSchema(Schema):
    id = fields.Integer()
    description = fields.String(allow_none=False)
    category = fields.String()
    user_id = fields.Integer(allow_none=False)
    vendor_id = fields.Integer(allow_none=False)
    date_created = fields.DateTime()
    last_updated = fields.DateTime()

    @post_load
    def make_item(self, data, **kwargs):
        return Alert(**data)
