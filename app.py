import os
from flask import Flask, request, render_template
from flask import send_from_directory
from api.api_loader import load_api
from flasgger import Swagger
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from helpers.jwt_verify import token_required
from flask_security import Security
from flask_mail import Mail, Message
from authCredentials import uploadFile
import json
import jwt
import config.config as config

SOURCE_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''

app = Flask(__name__)
mail = Mail(app)
app.config['MAIL_SERVER'] : 'smtp.gmail.com'
app.config['MAIL_PORT'] : 465
app.config['MAIL_USERNAME'] : 'zcerin.mathew@gmail.com'
app.config['MAIL_PASSWORD'] : 'titus...1'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['Authentication'] = True

def setup_routes(app):
    @app.route('/<path:path>')
    def static_files(path):
        return send_from_directory(os.path.join(SOURCE_ROOT, 'static'), path)

    @app.route("/upload", methods = ['POST'])
    @token_required
    def index():
        target = os.path.join(APP_ROOT,'images/')
        print(target)
        if not os.path.isdir(target):
            os.mkdir(target)
        uploaded = request.files.getlist("file")
        for file in uploaded:
            filename = file.filename
            destination = "/".join([target, filename])
            file.save(destination)
            ext = os.path.splitext(filename)
            if ext[1] == '.png':
                uploadFile(filename,filename,'image/png')
            else:
                uploadFile(filename,filename,'image/jpeg')
        result = json.dumps(returnobjforsuccess)
        return result

    @app.route('/login1')
    def index5():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/LoginSuccess')
    def loginSuccess():
        return render_template('loggedin.html')    

    @app.route("/registerSuccess", methods = ['POST'])
    def afterregister():
        token = request.form.get('token')
        print(token)

        # try:
            # msg = Message('Confirm Email',sender='zcerin.mathew@gmail.com',recipients=[email])
            # print(msg)
        email = jwt.decode(token, config.SECRET_KEY)
        print(email['email'])
        r = requests.get('https://accounts.google.com/o/oauth2/v2/auth?')
        #     msg = Message('Confirm Email',sender='zcerin.mathew@gmail.com',recipients=[email['email']])
        #     print(msg)
        #     link = 'http://127.0.0.1:5000/confirm-email'+token
        #     print(link)
        #     msg.body = 'Your link is {}'.format(link)
        #     print(msg.body)
        #     mail = app.config['mail']
        #     print(mail)
        #     mail.send(msg)
        #     returnobjforsuccess['token'] = token
        #     result = json.dumps(returnobjforsuccess)
        #     return result
        # except Exception as e:
        #     return str(e)
        msg = Message('Hello', sender = 'zcerin.mathew@gmail.com', recipients = ['sandra.mathew@cabotsolutions.com'])
        msg.body = "Hello Flask message sent from Flask-Mail"
        print(msg)
        mail.send(msg)
        return "Sent"
    

def create_app():
    Swagger(app)
    load_api(app)
    setup_routes(app)
    CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Origin"])
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(use_reloader=True, threaded=True, port=5000)
    
    
