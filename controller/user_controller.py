import config.config as config
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_restful import abort
from models.login_model import Login_model
import json
from flask import render_template, make_response

logins = Login_model()
returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''

class User():
    def login(self, email, password):
        user_details = logins.login(email, password)
        print(user_details)
        print("from user details")
        print(user_details)
        if user_details == 0:
            print("under user class")
            return 0
        else:
            print("from controller")
            print(user_details)
            return 1
            
          