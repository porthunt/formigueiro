import json
import pycurl
import StringIO
import cloudant


from StringIO import StringIO
from urllib import urlencode
from persistance.company.company import Company

'''
Class Backer


'''


class Backer(object):
    
    def __init__(self, _conn):
        self.conn = _conn

    def add(self, json_string):
        json.dumps(json_string)
        my_document = self.conn.connect().create_document(json_string)
        if my_document.exists():
            return 'OK'
        else:
            return 'ERROR'

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
        backers = list()
        for item in json.loads(response_buffer.getvalue())['rows']:
            temp = Company(self.conn).retrieve(company_id=item['value']['company_id'])[0]['value']
            temp['unit'] = item['value']['unit']
            backers.append(temp)
        return json.dumps(backers)
