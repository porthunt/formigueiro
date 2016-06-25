import configparser
import json
import os

from flask import Flask
from persistance.connect import Connection

app = Flask(__name__)
app_name = 'FooBar'

config = configparser.ConfigParser()
config.read('config.ini')
cloudant_credentials = config['cloudant']


@app.route('/api')
def index():
    return 'Welcome to the {} API!'.format(app_name)


@app.route('/api/test')
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
    return 'error accessing the API'

PORT = int(os.getenv('PORT', 8000))
if __name__ == '__main__':
    global conn
    conn = Connection(cloudant_credentials['user'],
                      cloudant_credentials['pwd'],
                      cloudant_credentials['host'],
                      cloudant_credentials['db'])

    app.run(host='localhost', port=PORT, debug=True)
