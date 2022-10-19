from flask import request, current_app
from flask_restful import Resource, abort
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

from app import db
from app.models.vendor import Vendor
from app.models.alert import Alert
from app.schemas.alert_schema import AlertSchema
from app.auth import token_required


class AlertResource(Resource):
    def get(self):
        alerts = Alert.query.all()
        return [AlertSchema().dump(alert) for alert in alerts], 200

    @token_required
    def post(self, current_user):
        req_json = request.get_json()
        try:
            alert = AlertSchema().load(req_json)
        except ValidationError as e:
            return e.messages, 400
        alert.user_id = current_user.id
        try:
            db.session.add(alert)
            db.session.commit()
        except IntegrityError as e:
            abort(500, message="Unexpected Error!")
        return "", 201