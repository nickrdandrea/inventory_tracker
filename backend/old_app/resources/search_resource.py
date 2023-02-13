from flask import request
from flask_restful import Resource, reqparse

from old_app.models import Item, Vendor
from old_app.db_utils import search_item
from old_app.schemas.item_schema import ItemSchema


class SearchResource(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('vendor_name', type = str, required = True,
            help = 'No vendor specified.')
        self.reqparse.add_argument('terms', type = str, required = True,
            help = 'No search terms provided.')
        super(SearchResource, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        vendor_name = args['vendor_name']
        terms = args['terms']
        items = search_item(terms)
        return [ItemSchema().dump(item) for item in items], 200