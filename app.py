import os
from flask import Flask, request
from flask import send_from_directory
from api.api_loader import load_api
from flasgger import Swagger
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from helpers.jwt_verify import token_required
from flask_security import Security
from flask_mail import Mail
from authCredentials import uploadFile
import json

SOURCE_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

returnobjforsuccess = {}
returnobjforsuccess['Result'] = 'Success'
returnobjforsuccess['status'] = 1
returnobjforsuccess['error'] = ''

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

def create_app(name=None):
    app = Flask(name or 'App')
    app.config['mail'] = Mail(app)
    Swagger(app)
    load_api(app)
    setup_routes(app)
    CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Origin"])
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(use_reloader=True, threaded=True, port=5000)
