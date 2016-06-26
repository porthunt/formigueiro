import json
import pycurl
import StringIO
import requests

from StringIO import StringIO
from persistance.company.company import Company

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
        else:
            r_url += 'all'

        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()

        resp_value = json.loads(response_buffer.getvalue())['rows']
        return json.dumps(resp_value)

    def campaign_total(self, campaign_id):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/backer/_view/campaign_total?key="{}"'.format(
            self.conn.host,
            self.conn.db,
            campaign_id)
        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        resp_value = json.loads(response_buffer.getvalue())['rows'][0]['value']['unit']
        return json.dumps(resp_value)

    def retrieve_comments(self, alchemyapi_credentials, campaign_id):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/comments/_view/by_campaign_id?key="{}"'.format(
                                                                                            self.conn.host,
                                                                                            self.conn.db,
                                                                                            campaign_id)
        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        comments = list()
        for item in json.loads(response_buffer.getvalue())['rows']:
            temp = item
            temp['author'] = Company(self.conn).retrieve(company_id=item['value']['company_id'])
            comments.append(temp)
        return json.dumps(comments)

    def retrieve_comment_content(self, comment_id):
        response_buffer = StringIO()
        curl = pycurl.Curl()
        r_url = 'https://{}.cloudant.com/{}/_design/comments/_view/by_comment_id?key="{}"'.format(
                                                                                           self.conn.host,
                                                                                           self.conn.db,
                                                                                           comment_id)
        curl.setopt(curl.URL, r_url)
        curl.setopt(curl.USERPWD, '%s:%s' % (self.conn.user, self.conn.pwd))
        curl.setopt(curl.WRITEFUNCTION, response_buffer.write)
        curl.perform()
        curl.close()
        resp_value = json.loads(response_buffer.getvalue())['rows'][0]['value']['comment']
        return resp_value

    def analyse_comment(self, url, alchemyapi_credentials, comment_id):
        try:
            data = 'apikey={}&outputMode=json&url={}/api/comment/id/{}'.format(alchemyapi_credentials['apikey'], url, comment_id)
            resp = requests.post(alchemyapi_credentials['url'], data=data)

            return json.dumps(resp.json())
        except:
            return 'ERROR'

    def add_comment(self, alchemyapi_credentials, json_string):
        json.dumps(json_string)
        my_document = self.conn.connect().create_document(json_string)
        if my_document.exists():
            my_document['mood'] = self.analyse_comment('http://formigueiro-back.mybluemix.net',
                                                       alchemyapi_credentials,
                                                       my_document['_id'])
            my_document.save()
            return 'OK'
        else:
            return 'ERROR'

    def update(self, **kwargs):
        pass
