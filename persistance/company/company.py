import json
import pycurl
#import StringIO

from StringIO import StringIO

'''
Class Company

add(name, city, state, cnpj, telephone, email) # add a company
retrieve(email='') # retrieves all companies. If has argument email, returns just that company
'''


class Company(object):

    def __init__(self, _conn):
        self.conn = _conn

    def add(self, _name, _city, _state, _cnpj, _telephone, _email, **kwargs):
        pass

    def retrieve(self, **kwargs):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/company/_view/'.format(self.conn.host, self.conn.db)

        if 'email' in kwargs:
            r_url += 'by_email?key="'+kwargs['email']+'"'
        elif 'company_id' in kwargs:
            r_url += 'by_company_id?key="' + kwargs['company_id'] + '"'
        else:
            r_url += 'all'

        print(r_url)
        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        resp_value = json.loads(response_buffer.getvalue())['rows']
        return resp_value

    def update(self, **kwargs):
        pass
