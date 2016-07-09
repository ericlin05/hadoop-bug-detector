from HTMLParser import HTMLParser
from StringIO import StringIO
from bs4 import BeautifulSoup
import re, cgi
import pycurl

class ApacheJiraParser:
    def __init__(self, apache_id):
        self.apache_id = apache_id
        self.url = 'https://issues.apache.org/jira/browse/' + apache_id
        self.data = "" 

    def parse(self):
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        
        div = BeautifulSoup(
	          buffer.getvalue(), 
		  'html.parser'
              ).find(id='descriptionmodule')
        
        content = BeautifulSoup(
	              str(div), 
		      'html.parser'
	          ).find('p');
        
        tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
        self.data = cgi.escape(tag_re.sub('', str(content)))

        return self

    def write(self):
        text_file = open("data/" + self.apache_id, "w")
        text_file.write(self.data)
        text_file.close()

