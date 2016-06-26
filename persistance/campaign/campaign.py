import json
import pycurl
import StringIO

from StringIO import StringIO

'''
Class Campaign


'''


class Campaign(object):

    def __init__(self, _conn):
        self.conn = _conn

    def add(self, _author, _name, _description, _original_unit_price, _end_date, **kwargs):
        pass

    def retrieve(self, **kwargs):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/campaign/_view/'.format(self.conn.host, self.conn.db)

        if 'campaign_id' in kwargs:
            r_url += 'by_campaign_id?key="'+kwargs['campaign_id']+'"'
        elif 'author' in kwargs:
            r_url += 'by_author?key="'+kwargs['author']+'"'
        elif 'name' in kwargs:
            r_url += 'by_name?key="'+kwargs['name']+'"'
        elif 'category' in kwargs:
            r_url += 'by_category?key="'+kwargs['category']+'"'

        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        resp_value = json.loads(response_buffer.getvalue())['rows']
        return json.dumps(resp_value)

    def update(self, **kwargs):
        pass
