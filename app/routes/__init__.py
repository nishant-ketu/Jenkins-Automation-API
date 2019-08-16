'''__init__.py  file'''
from flask import Blueprint
from flask_restplus import Api
from app import app
from .home import api as home_api

swagger = Blueprint('JENKINS_AUTOMATION-API', __name__, url_prefix='/api')
api = Api(swagger, version='1.0', title='JENKINS AUTOMATIONC API')

api.add_namespace(home_api)

app.register_blueprint(swagger)
parser = api.parser()
