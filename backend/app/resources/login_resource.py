from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from app.models.user import User


class LoginResource(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
            help = 'No username provided.')
        self.reqparse.add_argument('password', type = str, required = True,
            help = 'No password provided.')
        super(LoginResource, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        password = args['password']

        user = User.query.filter_by(name=username).first()
        if not user or not user.check_password(password):
            return {"message": "Wrong username or password."}, 401

        access_token = create_access_token(identity=user)
        return {"access_token": access_token}, 200
