from HTMLParser import HTMLParser
from StringIO import StringIO
from bs4 import BeautifulSoup
import re, cgi
import pycurl
import logging

class ApacheJiraParser:
    def __init__(self, apache_id):
        self.apache_id = apache_id
        self.url = 'https://issues.apache.org/jira/browse/' + apache_id
        self.data = "" 

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def parse(self):
        self.logger.info("Retrieving JIRA: " + self.url)

        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        
        content = str(
            BeautifulSoup(
                buffer.getvalue(),
            'html.parser'
            ).find(id='descriptionmodule')
        )
        self.logger.info("JIRA retrieved")
        
        if content is None or content == 'None' or content.strip() == "":
            self.logger.info('No description was found for ID: %s', self.apache_id)
        else:
            tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
            self.data = cgi.escape(tag_re.sub('', content))
            self.logger.info("Striping HTML tags")

            return self

    def write(self):
        if not self.data:
            self.logger.info('No description was found for ID: %s, skipping writing file..', self.apache_id)
            return

        text_file = open("data/" + self.apache_id, "w")
        text_file.write(self.data)
        text_file.close()

