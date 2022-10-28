import json
from flask import request
from flask_restful import Resource

from app.models.user import User
from app import db


class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(name=data["name"])
        new_user.set_password(data["password"])
        try:
            db.session.add(new_user)
            db.session.commit()
            return {"message": "registeration successful"}, 201
        except:
            return {"message": "registeration failed"}, 500
