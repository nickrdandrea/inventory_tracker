from flask import request, current_app
from flask_restful import Resource, abort
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

from app import db
from app.models.vendor import Vendor
from app.models.item import Item
from app.schemas.item_schema import ItemSchema
from app.auth_util import token_required


class ItemResource(Resource):
    def get(self):
        items = Item.query.all()
        return [ItemSchema().dump(item) for item in items], 200

    @token_required
    def post(self, current_user):
        req_json = request.get_json()
        vendor_id = self._get_vendor_id(req_json["vendor"])
        for item_json in req_json["items"]:
            try:
                item = ItemSchema().load(item_json)
            except ValidationError as e:
                return e.messages, 400
            insert_values = ItemSchema(exclude=["id", "date_created"]).dump(item)
            insert_values["vendor_id"] = vendor_id
            self._upsert_item(insert_values)
        return "", 201

    def _get_vendor_id(self, vendor_name):
        vendor = Vendor.query.filter_by(name=vendor_name).first()
        if not vendor:
            abort(422, message=f"{vendor_name} is not a valid vendor.")
        return vendor.id

    def _upsert_item(self, insert_values):
        insert_stmt = insert(Item).values(insert_values)
        # sqlite does not support on_conflict_do_update
        if 'sqlite' not in current_app.config['SQLALCHEMY_DATABASE_URI']:
            insert_stmt = insert_stmt.on_conflict_do_update(
                constraint="_description_vendor_id_uc", set_={"last_updated": db.func.now()}
            )
        try:
            db.session.execute(insert_stmt)
            db.session.commit()
        except IntegrityError as e:
            abort(500, message="Unexpected Error!")
