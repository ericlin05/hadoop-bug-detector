from StringIO import StringIO
from bs4 import BeautifulSoup
import re, cgi
import pycurl
from lib.Logger import Logger

# This class scans through a given Apache JIRA ID's description part on
# the JIRA web page, and determine if there is any Exception or "Caused by"
# word, we will consider it as a BUG JIRA and we will capture it and store
# in a local file
class ApacheJiraParser:
    def __init__(self, type, apache_id):
        self.type = type
        self.apache_id = str(apache_id)
        self.full_id = self.type.upper() + '-' + self.apache_id
        self.url = 'https://issues.apache.org/jira/browse/' + self.full_id
        self.data = "" 
        self.logger = Logger(__name__)

    def parse(self):
        self.logger.info("Retrieving JIRA: %s", self.url)

        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.url)
        c.setopt(c.WRITEFUNCTION, buffer.write)
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
            self.logger.info('No description was found for ID: %s', self.full_id)
        elif re.search(".*Exception.*", content) is None and re.search(".*Caused by.*", content) is None:
            self.logger.info('No Exception or Cause By found for ID: %s', self.full_id)
        else:
            # strip HTML tags
            tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
            self.data = cgi.escape(tag_re.sub('', content))
            self.logger.info("Striping HTML tags")

        return self

    def write(self):
        if not self.data:
            self.logger.info('No data was found for ID: %s, skipping writing file..', self.full_id)
            return

        text_file = open("data/" + self.type.lower() + '/' + self.full_id, "w")
        text_file.write(self.data)
        text_file.close()

