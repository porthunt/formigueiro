import uuid

from cloudant import Cloudant
from cloudant.query import Query


class Connection(object):

    def __init__(self, _user, _pwd, _account, _db):
        self.client = Cloudant(_user, _pwd, account=_account)
        self.user = _user
        self.host = _account
        self.pwd = _pwd
        self.db = _db

    def connect(self):
        self.client.connect()
        return self.client[self.db]

    def disconnect(self):
        self.client.disconnect()

    def register_error(self, e, author):
        try:
            err_code = uuid.uuid4()
            doc = {
                'doc_type': 'error',
                'code': str(err_code),
                'message': str(e)
            }
            self.database.create_document(doc)
            return err_code
        except:
            return None

    def test_connection(self):
        fields = ['_id']
        query = Query(self.connect(), selector={'_id': {'$gt': 0}, 'doc_type': 'test'}, fields=fields)
        self.disconnect()
        return query.result
