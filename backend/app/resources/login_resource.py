import datetime
import jwt
import os
from flask import request
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from app.models.user import User


class LoginResource(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
            help = 'No username provided', location = 'json')
        self.reqparse.add_argument('password', type = str, required = True,
            help = 'No password provided', location = 'json')
        super(LoginResource, self).__init__()

    def post(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return {"message": "Invalid authorization"}, 422

        user = User.query.filter_by(name=auth.username).first()
        if not user:
            return {"message": "User not found."}, 404

        if user.check_password(auth.password):
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
