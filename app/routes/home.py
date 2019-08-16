from flask_restplus import Namespace, Resource
import requests
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
      response = requests.post('http://jenkins_host/job/MY_JOB_NAME/build', auth=('username', 'API_TOKEN'))
      return response
      
