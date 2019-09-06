
import jwt
from flask import request


def is_login():
    username = login_user()
    return not username is None


def login_user():
    token = request.cookies.get('token')
    if not token:
        token = request.args.get("token")
    if not token:
        token = request.form.get("token")
    if not token:
        return None
    else:
        try:
            result = jwt.decode(token, 'secret', algorithms=['HS256'])
            if not result or not result['username']:
                return None
            else:
                return result['username']
        except jwt.ExpiredSignatureError:
            return None
