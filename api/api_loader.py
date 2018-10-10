from flask_restful import Api, Resource
from flask import send_from_directory
from api.login import Login
import os
from flask.views import MethodView
from flask_restful.utils import cors

def load_api(app):
    apis = Api(app)
    apis.decorators=[cors.crossdomain(origin='*')]
    apis.add_resource(Login, '/login')
    