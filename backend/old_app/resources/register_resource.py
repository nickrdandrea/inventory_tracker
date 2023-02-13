from flask_restful import Resource, reqparse

from old_app import db
from old_app.models.user import User


class RegisterResource(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
            help = 'No username provided.')
        self.reqparse.add_argument('password', type = str, required = True,
            help = 'No password provided.')
        super(RegisterResource, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        username = args['username']
        password = args['password']
        new_user = User(name=username)
        new_user.set_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return {"message": "Registeration successful."}, 201
        except:
            return {"message": "Registeration failed."}, 500
