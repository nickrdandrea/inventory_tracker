import os
import jwt
from flask import request
from functools import wraps

from app.models.user import User

def create_token():
        token = jwt.encode(
            {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=45),
            },
            os.getenv("SECRET_KEY"),
            "HS256",)
        return token

def token_required(f):
    @wraps(f)
    def decorator(self, *args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]
        else:
            return "Token is missing.", 401
        try:
            decoded = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            current_user = User.query.filter_by(id=decoded['id']).first()
        except:
            return "Token is invalid.", 401

        return f(self, current_user, *args, **kwargs)
    return decorator
