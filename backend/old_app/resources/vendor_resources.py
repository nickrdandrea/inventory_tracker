from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError
from sqlite3 import IntegrityError

from old_app.models import Item, Vendor
from old_app.schemas import ItemSchema, VendorSchema
from old_app import db

def get_vendor_by_name(vendor_name):
    vendor_name = vendor_name.lower().strip()
    vendor_name = vendor_name.replace("-", " ")
    vendor = Vendor.query.where(db.func.lower(Vendor.name) == vendor_name).first()
    return vendor

class VendorResource(Resource):

    def get(self, vendor_name):
        vendor = get_vendor_by_name(vendor_name)
        return VendorSchema().dump(vendor), 200

class VendorItemResource(Resource):

    def get(self, vendor_name, item_id):
        vendor = get_vendor_by_name(vendor_name)
        item = Item.query.where(Item.vendor_id == vendor.id).where(Item.id == item_id).first()
        return ItemSchema().dump(item), 200

class VendorsResource(Resource):

    def get(self):
        vendors = Vendor.query.all()
        return [VendorSchema().dump(vendor) for vendor in vendors]

    # def post(self, current_user):
    #     req_json = request.get_json()
    #     try:
    #         vendor = VendorSchema().load(req_json)
    #     except ValidationError as e:
    #         return e.messages, 400
    #     try:
    #         db.session.add(vendor)
    #         db.session.commit()
    #     except IntegrityError as e:
    #         abort(500, message="Unexpected Error!")
    #     return "", 201
