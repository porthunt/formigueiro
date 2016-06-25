import json
import pycurl
import StringIO

from StringIO import StringIO

'''
Class Backer


'''


class Backer(object):
    
    def __init__(self, _conn):
        self.conn = _conn

    def add(self, company_id, campaign_id, unit):
        pass

    def remove(self, company_id, campaign_id):
        pass

    def update(self, company_id, campaign_id, unit):
        pass

    def retrieve(self, **kwargs):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/backer/_view/'.format(self.conn.host, self.conn.db)

        if 'campaign_id' in kwargs:
            r_url += 'by_campaign_id?key="' + kwargs['campaign_id'] + '"'
        elif 'company_id' in kwargs:
            r_url += 'by_company_id?key="' + kwargs['company_id'] + '"'

        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        resp_value = json.loads(response_buffer.getvalue())['rows']
        return json.dumps(resp_value)
