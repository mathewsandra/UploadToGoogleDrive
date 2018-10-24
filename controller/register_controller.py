import config.config as config
import jwt
from flask_mail import Mail, Message
from flask_restful import abort
import json
import smtplib
from flask import current_app
from models.register_model import register_model
import datetime
from flask import jsonify, make_response

reg = register_model()
returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''
returnobjforfailure = {}
returnobjforfailure['error'] = 'Invalid username or password'
returnobjforfailure['Result'] = 'Failed'
returnobjforfailure['status'] = 0


# s = URLSafeTimedSerializer(config.SECRET_KEY)
class REG():
    def reg1(self, email, password, confirmPassword):
        email1 = email
        result = reg.register_undermodel( email, password, confirmPassword)
        print('yes yes yes')
        # token = s.dumps(email, salt='email-confirm')
        if result == 1:

            token = jwt.encode({'email' : email1, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, config.SECRET_KEY)
            tokenstring = jsonify({'token' : token.decode('UTF-8')})
            print('yyyyyiiiipppeeeee')
            print(tokenstring)
        
        # # try:
        # msg = Message('Confirm Email',sender='zcerin.mathew@gmail.com',recipients=[email])
        # print(msg)
        # link = 'http://127.0.0.1:5000/confirm-email'+token
        # print(link)
        # msg.body = 'Your link is {}'.format(link)
        # print(msg.body)
        # # mail = Mail()
        # mail = current_app.config['mail']
        # print(mail)
        # mail.send(msg)
            # returnobjforsuccess['token'] = tokenstring
            # print(returnobjforsuccess['token'])
            # resultsuccess = json.dumps(returnobjforsuccess)
            return tokenstring
           
        
        else:
            result = json.dumps(returnobjforsuccess)
            return result

