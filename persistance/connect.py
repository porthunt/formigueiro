from cloudant import Cloudant
from cloudant.query import Query


class Connection(object):

    def __init__(self, _user, _pwd, _account, _db):
        self.client = Cloudant(_user, _pwd, account=_account)
        self.client.connect()
        self.db = self.client[_db]

    def disconnect(self):
        self.client.disconnect()

    def test_connection(self):
        fields = ['_id']
        query = Query(self.db, selector={'_id': {'$gt': 0}, 'doc_type': 'test'}, fields=fields)
        return query.result
