from flask_restful import Resource, abort
from flask import jsonify, request
from flask_restful import reqparse
from flasgger.utils import swag_from
from controller.user_controller import User
from helpers.jwt_verify import token_required

user_controller = User()

class Login(Resource):

    @swag_from('../swagg/register.yml')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required')
        parser.add_argument('password', type=str, required=True, help='password required')
        args = parser.parse_args()
        del parser
        return user_controller.login(args['email'], args['password'])
        

    