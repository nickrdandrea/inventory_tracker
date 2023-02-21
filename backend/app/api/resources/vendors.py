from flask import request
from flask_restful import Resource

from app.models import Vendor
from app.adapters.repositories  import VendorRepository

class VendorResource(Resource):
    def get(self):
        return 200