from flask import request, current_app
from flask_restful import Resource, abort
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert

from old_app import db
from old_app.models.vendor import Vendor
from old_app.models.alert import Alert
from old_app.schemas.alert_schema import AlertSchema


class AlertResource(Resource):
    def get(self):
        alerts = Alert.query.all()
        return [AlertSchema().dump(alert) for alert in alerts], 200

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