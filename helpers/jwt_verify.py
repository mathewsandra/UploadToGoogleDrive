from functools import wraps
from flask import request
from flask_restful import abort
from flask import jsonify
import jwt
import config.config as config


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.form.get('token')
        print(token)
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403

        try:
            data = jwt.decode(token, config.SECRET_KEY)

        except:
            return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)

    return decorated