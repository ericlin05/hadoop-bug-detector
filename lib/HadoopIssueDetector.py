import re, sys, os
from Logger import Logger

sys.path.append(os.path.abspath('conf'))
import settings

class HadoopIssueDetector:
    def __init__(self, type, filename):
        self.logger = Logger(__name__)
        self.found = {}
        self.contents = []
        self.type = type

        self.logger.info("Reading file: %s", filename)
        with open(filename, 'r') as f:
            self.contents = f.read()

        self.logger.info("Total of %d lines read", len(self.contents))

    def detect(self):
        for pattern, message in settings.LOG_PATTERNS[self.type].iteritems():
            regexp = ".*" + pattern + ".*"
            if re.search(regexp, self.contents):
                self.logger.info("Found line: \"%s\" matches \"%s\" on line %d", self.contents, pattern, 1)
                self.found[message] = 1