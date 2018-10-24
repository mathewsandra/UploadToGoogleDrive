from flask_restful import Resource, abort
from flask import jsonify, request
from flask_restful import reqparse
from flasgger.utils import swag_from
from controller.user_controller import User
from helpers.jwt_verify import token_required
import json
import jwt

user_controller = User()

sss={}
sss["auth_token"]="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzYW5kcmFAZ21haWwuY29tIjoic2FuZHJhQGdtYWlsLmNvbSIsImV4cCI6MTU0MDI4NzM0Mn0.8J9AM0UIHdr_xwuOt0uESNliN0uN6QQBTuhj1yT9038"
returnobjforfailure = {}
returnobjforfailure['error'] = 'Invalid username or password'
returnobjforfailure['Result'] = 'Failed'
returnobjforfailure['status'] = 0
returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''
class Login(Resource):

    @swag_from('../swagg/register.yml')
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required')
        parser.add_argument('password', type=str, required=True, help='password required')
        args = parser.parse_args()
        del parser
        test = user_controller.login(args['email'], args['password'])
        if test == 0:
            print("inside if")
            result1 = json.dumps(returnobjforfailure)
            print(result1) 
            return "Failed"
        else:
            result1 = json.dumps(returnobjforsuccess)
            print(result1) 
            return "Success"
        
    def get(self):
        # result = json.dumps(returnobjforfailure)
        # return result
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='email required')
        parser.add_argument('password', type=str, required=True, help='password required')
        args = parser.parse_args()
        del parser
        test = user_controller.login(args["email"], args["password"])
        print(test)
        # result = jsonify(returnobjforfailure)
        if test == 0:
            print("inside if")
            result1 = json.dumps(returnobjforfailure)
            print(result1) 
            return "Failed"
        else:
            result1 = json.dumps(returnobjforsuccess)
            print(result1) 
            return "Success"




    