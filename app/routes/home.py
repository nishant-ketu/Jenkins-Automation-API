from flask_restplus import Namespace, Resource
from flask import jsonify
import requests
from app import app
import json

api = Namespace(
    'home', description='JENKINS')
parser = api.parser()

@api.route('/build')
class build(Resource):
    @api.doc(parser=parser)
    def post(self):
      res=requests.post('http://127.0.0.1:8080/job/Job1/build', auth=('nishant-ketu', '117d3925696a12bec26687dbb331d64d3a'))
      return res.status_code

    @api.doc(parser=parser)
    def get(self):
      response = requests.get('http://10.0.2.15:8080/view/All/api/json', auth=('nishant-ketu', '117d3925696a12bec26687dbb331d64d3a'))
      return json.loads(response.text)

@api.route('/create')
class create(Resource):
    @api.doc(parser=parser)
    def post(self):
      headers = {
        'content-Type': 'application/xml',
      }
      params = (
        ('name', 'A_job'),
      )
      data = '<project><builders/><publishers/><buildwrappers/></project>'
      response = requests.post('http://10.0.2.15:8080/createItem', headers=headers, params=params, data=data, auth=('nishant-ketu', '117d3925696a12bec26687dbb331d64d3a'))
      return response.status_code
