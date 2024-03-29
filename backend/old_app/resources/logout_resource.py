from flask_restful import Resource
from flask_jwt_extended import unset_jwt_cookies
from flask import jsonify


class LogoutResource(Resource):
    
    def post(self):
        response = jsonify({ "message": "logout successful" })
        unset_jwt_cookies(response)
        return response