import config.config as config
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import url_for
from flask_mail import Mail, Message
from flask_restful import abort
import json
import smtplib
from flask import current_app
from itsdangerous import URLSafeTimedSerializer
from models.register_model import register_model


reg = register_model()
returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''
s = URLSafeTimedSerializer(config.SECRET_KEY)
class REG():
    def reg1(self, email, password, confirmPassword):
        result = reg.register_undermodel( email, password, confirmPassword)
        token = s.dumps(email, salt='email-confirm')
        print(token)
        # try:
        msg = Message('Confirm Email',sender='zcerin.mathew@gmail.com',recipients=[email])
        print(msg)
        link = 'http://127.0.0.1:5000/confirm-email'+token
        print(link)
        msg.body = 'Your link is {}'.format(link)
        print(msg.body)
        # mail = Mail()
        mail = current_app.config['mail']
        print(mail)
        mail.send(msg)
        returnobjforsuccess['token'] = token
        result = json.dumps(returnobjforsuccess)
        return result
        # except Exception as e:
        #     return str(e)
       
        
