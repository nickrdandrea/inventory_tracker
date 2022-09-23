import os
import jwt
from flask import jsonify, request
from functools import wraps

from app.models.user import User


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "x-access-tokens" in request.headers:
            token = request.headers["x-access-tokens"]

        if not token:
            return jsonify({"message": "a valid token is missing"})
        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            # current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({"message": "token is invalid"})

        return f(*args, **kwargs)

    return decorator
