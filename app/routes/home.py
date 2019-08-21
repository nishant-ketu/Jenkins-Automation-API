from flask_restplus import Namespace, Resource, fields
from flask import jsonify
import requests
from app import app
import json
import time

api = Namespace(
    'home', description='JENKINS')
parser = api.parser()

Jenkins_configuration = api.model('Jenkins Configuration', {
    'Github URL': fields.Url('github_url'),
    'github username': fields.String('github_username'),
    'github password': fields.String('github_password')})


Build_configuration = api.model('Build Configuration', {
    'Job_name': fields.String('Job Name'),
    'Github_URL': fields.Url('Github_URL'),
    'Github_branch': fields.String('Github_branch'),
    'command': fields.String('commands')})

@api.route('/build')
class build(Resource):
    @api.expect(Build_configuration)
    def post(self):
      params = (
        ('Github_URL', api.payload['Github_URL']),
        ('Github_branch', api.payload['Github_branch']),
        ('commands', api.payload['command']),
      )
      response = requests.post('http://127.0.0.1:8080/job/'+ api.payload['Job_name']+'/buildWithParameters', params=params, auth=('nishant', '11047f6c472c8d601da909a63377d31352'))
      time.sleep(15)
      response = requests.get('http://127.0.0.1:8080/job/A_new_job/lastBuild/api/json', auth=('nishant', '11047f6c472c8d601da909a63377d31352'))
      # print(response.text)
      res = json.loads(response.text)
      if res['building']:
        time.sleep(10)
      else:
        if res['result'] == "SUCCESS":
          return "Build #"+ res['id'] +" was successfull"
        else:
          return "Build #"+ res['id'] +" has failed"


    @api.doc(parser=parser)
    def get(self):
      response = requests.get('http://127.0.0.1:8080/view/All/api/json', auth=('nishant', '11047f6c472c8d601da909a63377d31352'))
      print(response.text)
      jobsjson = json.loads(response.text)
      joblist = []
      for i in jobsjson["jobs"]:
        joblist.append(i["name"])
      return joblist

@api.route('/create')
class create(Resource):
  @api.expect(Jenkins_configuration)
  def post(self):
    headers = {
      'content-Type': 'text/xml',
    }
    params = (
      ('name', 'A_new_job'),
    )
    data = open('/home/nishantketu/Documents/JenkinsAutomation/config.xml', 'rb').read()
    
    response = requests.post('http://127.0.0.1:8080/createItem', headers=headers, params=params, data=data, auth=('nishant', '11047f6c472c8d601da909a63377d31352'))
    return response.status_code

@api.route('/status')
class status(Resource):
  @api.doc(parser=parser)
  def get(self):
    response = requests.get('http://127.0.0.1:8080/job/A_new_job/lastBuild/api/json', auth=('nishant', '11047f6c472c8d601da909a63377d31352'))
    # print(response.text)
    res = json.loads(response.text)
    if res['building']:
      time.sleep(60)
    else:
      if res['result'] == "SUCCESS":
        return "Job was successfully build"
      else:
        return "Job has failed"
            