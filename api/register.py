from flask_restful import Resource, abort
from flask import jsonify, request
from flask_restful import reqparse
from flasgger.utils import swag_from
from controller.register_controller import REG

register_controller = REG()

class Reg(Resource):

    @swag_from('../swagg/register.yml')
    def post(self):
        print("///////////////////")
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required')
        parser.add_argument('password', type=str, required=True, help='password required')
        parser.add_argument('confirmPassword', type=str, required=True, help='confirm password required')
        args = parser.parse_args()
        del parser
        print("///////////////////")
        print (args)
        return register_controller.reg1(args['email'], args['password'], args['confirmPassword'])
   
   
