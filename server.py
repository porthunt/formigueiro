import configparser
import json
import os

from flask import Flask
from flask import request
from flask_cors import CORS
from persistance.connect import Connection
from persistance.company.company import Company
from persistance.campaign.campaign import Campaign
from persistance.backer.backer import Backer

app = Flask(__name__)
CORS(app)
app_name = 'FooBar'

config = configparser.ConfigParser()
config.read('config.ini')
cloudant_credentials = config['cloudant']
alchemyapi_credentials = config['alchemy-api']


@app.route('/api')
def index():
    return 'Welcome to the {} API!'.format(app_name)


@app.route('/api/company', methods=['GET'])
@app.route('/api/company/<email>', methods=['GET'])
def company(email=None):
    if email is not None:
        return Company(conn).retrieve(email=email)
    else:
        return Company(conn).retrieve()


@app.route('/api/campaign', methods=['GET'])
@app.route('/api/campaign/id/<campaign_id>', methods=['GET'])
@app.route('/api/campaign/name/<name>', methods=['GET'])
@app.route('/api/campaign/category/<category>', methods=['GET'])
@app.route('/api/campaign/author/<author>', methods=['GET'])
def campaign(campaign_id=None, name=None, category=None, author=None):
    if campaign_id is not None:
        return Campaign(conn).retrieve(campaign_id=campaign_id)
    elif name is not None:
        return Campaign(conn).retrieve(name=name)
    elif author is not None:
        return Campaign(conn).retrieve(author=author)
    elif category is not None:
        return Campaign(conn).retrieve(category=category)
    else:
        return Campaign(conn).retrieve()


@app.route('/api/campaign/id/<campaign_id>/total', methods=['GET'])
def campaign_total(campaign_id=None):
    if campaign_id is None:
        return 'campaign not found'
    else:
        return Campaign(conn).campaign_total(campaign_id=campaign_id)


@app.route('/api/campaign/id/<campaign_id>/comments', methods=['GET'])
def campaign_comments(campaign_id=None):
    if campaign_id is None:
        return 'campaign not found'
    else:
        return Campaign(conn).retrieve_comments(alchemyapi_credentials=alchemyapi_credentials, campaign_id=campaign_id)


@app.route('/api/comment/id/<comment_id>', methods=['GET'])
def comment_content(comment_id=None):
    return Campaign(conn).retrieve_comment_content(comment_id=comment_id)

'''
@app.route('/api/comment/id/<comment_id>/analyse', methods=['GET'])
def analyse_comment(comment_id=None):
    return Campaign(conn).analyse_comment(alchemyapi_credentials=alchemyapi_credentials,
                                          url="http://formigueiro-back.mybluemix.net",
                                          comment_id=comment_id)
'''


@app.route('/api/backer/campaign_id/<campaign_id>', methods=['GET'])
@app.route('/api/backer/company_id/<company_id>', methods=['GET'])
def backer(campaign_id=None, company_id=None):
    if campaign_id is not None:
        return Backer(conn).retrieve(campaign_id=campaign_id)
    elif company_id is not None:
        return Backer(conn).retrieve(company_id=company_id)
    else:
        return 'campaign not found'


@app.route('/api/backer/add', methods=['PUT'])
def add_backer():

    try:

        if request.json['doc_type'] != 'backer' or not request.json:
            raise Exception('')

        add_backer = {
            'doc_type': request.json['doc_type'],
            'campaign_id': request.json['campaign_id'],
            'company_id': request.json['company_id'],
            'unit': request.json['unit']
        }
        return Backer(conn).add(add_backer)
    except:
        return 'ERROR'


@app.route('/api/comment/add', methods=['PUT'])
def add_comment():

    try:
        if request.json['doc_type'] != 'comment' or not request.json:
            raise Exception('')

        comment = {
            "doc_type": request.json['doc_type'],
            "campaign_id": request.json['campaign_id'],
            "company_id": request.json['company_id'],
            "comment": request.json['comment']
        }
        Campaign(conn).add_comment(alchemyapi_credentials, comment)
        return 'OK'
    except:
        return 'ERROR'

@app.route('/api/test-api')
def test_connection():
    lst = list()
    for document in conn.test_connection():
        lst.append(document)
    return json.dumps(lst)


@app.errorhandler(404)
def page_not_found(e):
    return 'api not found'


@app.errorhandler(500)
def internal_server_error(e):
    return 'API error'

PORT = int(os.getenv('PORT', 8000))
if __name__ == '__main__':
    global conn
    conn = Connection(cloudant_credentials['user'],
                      cloudant_credentials['pwd'],
                      cloudant_credentials['host'],
                      cloudant_credentials['db'])

    app.run(host='0.0.0.0', port=PORT)
