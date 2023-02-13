from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from base64 import b64decode

from old_app.models.user import User

class LoginResource(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('Authorization', location='headers', required= True)
        super(LoginResource, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        auth_type, encoded_credentials = args['Authorization'].split()
        if auth_type.lower() == 'basic':
            credentials = b64decode(encoded_credentials).decode().split(':')
        else:
            return {"message": "Invalid authentication type."}, 401
        
        username = credentials[0]
        password = credentials[1]
        user = User.query.filter_by(name=username).first()
        if not user or not user.check_password(password):
            return {"message": "Wrong username or password."}, 401
        
        access_token = create_access_token(identity=user)
        return { "username": user.name, "id": user.id, "access_token": access_token }, 200
