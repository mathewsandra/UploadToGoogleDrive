import config.config as config
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_restful import abort
from models.login_model import Login_model
import json

logins = Login_model()
returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''
returnobjforfailure = {}
returnobjforfailure['error'] = 'Invalid username or password'
returnobjforfailure['Result'] = 'Failed'
returnobjforfailure['status'] = 0

class User():
    def login(self, email, password):
        user_details = logins.login(email, password)
        print(user_details)
        if user_details == 0:
            print("under user class")
            result = json.dumps(returnobjforfailure) 
            return result
        else:
            return user_details