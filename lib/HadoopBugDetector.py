import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from Logger import Logger
from difflib import SequenceMatcher

class HadoopBugDetector:
    def __init__(self, filename, jiraLoader):
        self.jiraLoader = jiraLoader
        self.logger = Logger(__name__)

        self.logger.info("Reading file: " + filename)
        with open(filename, 'r') as f:
            self.data = f.read().split('\n')

    def detect(self):
        for line in self.data:
            for jiraID in self.jiraLoader.lines:
                for l in self.jiraLoader.lines[jiraID]:
                    ratio = SequenceMatcher(None, line, l).ratio()
                    if ratio > 0.5:
                        self.logger.info("Similarity ratio: " + str(ratio) + " found in JIRA: " + jiraID)
                        self.logger.info("JIRA line: " + l)
                        self.logger.info("File line: " + line)
                        return True

        return False


