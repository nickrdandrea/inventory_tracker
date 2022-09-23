import datetime
import jwt
import os
from flask import request
from flask_restful import Resource
from werkzeug.security import check_password_hash

from app.models.user import User


class LoginResource(Resource):
    def post(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {"message": "Invalid authorization"}, 422

        user = User.query.filter_by(name=auth.username).first()
        if not user:
            return {"message": "User not found."}, 404

        if check_password_hash(user.password_hash, auth.password):
            token = jwt.encode(
                {
                    "id": user.id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45),
                },
                os.getenv("SECRET_KEY"),
                "HS256",
            )
            return {"token": token}, 200

        return {"message": "Could not verify"}, 401
