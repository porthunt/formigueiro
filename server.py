import configparser
import json
import os

from flask import Flask
from persistance.connect import Connection
from persistance.company.company import Company
from persistance.campaign.campaign import Campaign

app = Flask(__name__)
app_name = 'FooBar'

config = configparser.ConfigParser()
config.read('config.ini')
cloudant_credentials = config['cloudant']


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
        return 'campaign not found'


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

    app.run(host='localhost', port=PORT, debug=True)
