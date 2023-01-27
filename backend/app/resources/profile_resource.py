from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from app import db
from app.models.user import User

class ProfileResource(Resource):
    method_decorators = [jwt_required()]
    
    def get(self):
        current_user = get_jwt_identity()
        return { "message": current_user }, 200