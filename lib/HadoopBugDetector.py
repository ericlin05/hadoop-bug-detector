import os, sys, re
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from Logger import Logger
from difflib import SequenceMatcher

class HadoopBugDetector:
    def __init__(self, filename, jiraLoader):
        self.jiraLoader = jiraLoader
        self.logger = Logger(__name__)
        self.matchedJira = []
        self.data = []

        self.logger.info("Reading file: %s", filename)
        with open(filename, 'r') as f:
            for line in f:
                if re.search(".*Caused by.*", line):
                    self.data.append(line.strip())

        self.logger.info("Total of %d lines read", len(self.data))

    def detect(self):
        for line in self.data:
            for jiraID in self.jiraLoader.lines:
                for l in self.jiraLoader.lines[jiraID]:
                    ratio = SequenceMatcher(None, line, l).ratio()
                    if ratio > 0.5:
                        self.logger.info("")
                        self.logger.info("Similarity ratio: %s found in JIRA %s", str(ratio), jiraID)
                        self.logger.info("JIRA line: %s", l)
                        self.logger.info("File line: %s", line)

                        self.matchedJira.append(jiraID)
                        return
