from flask_restplus import Namespace, Resource
from requests import get, post
from app import app

api = Namespace(
    'home', description='JENKINS')
parser = api.parser()


@api.route('')
class homepage(Resource):
    @api.doc(parser=parser)
    def get(self):
      return "we are on home"

    @api.doc(parser=parser)
    def post(self):
      post()
      
