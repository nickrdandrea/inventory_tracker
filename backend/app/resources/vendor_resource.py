from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError
from sqlite3 import IntegrityError

from app.models.vendor import Vendor
from app.schemas.vendor_schema import VendorSchema
from app import db


class VendorResource(Resource):
    def get(self):
        vendors = Vendor.query.all()
        return [VendorSchema().dump(vendor) for vendor in vendors]

    def post(self, current_user):
        req_json = request.get_json()
        try:
            vendor = VendorSchema().load(req_json)
        except ValidationError as e:
            return e.messages, 400
        try:
            db.session.add(vendor)
            db.session.commit()
        except IntegrityError as e:
            abort(500, message="Unexpected Error!")
        return "", 201
