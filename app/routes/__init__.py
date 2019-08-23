'''__init__.py  file'''
from flask import Blueprint
from flask_restplus import Api
from app import app
from .home import api as home_api

swagger = Blueprint('JENKINS_AUTOMATION_API', __name__, url_prefix='/api')
api = Api(swagger, version='2.1', title='JENKINS AUTOMATION API')

api.add_namespace(home_api)

app.register_blueprint(swagger)
parser = api.parser()
