import re, sys, os
from Logger import Logger
from difflib import SequenceMatcher
from Utils import Utils

sys.path.append(os.path.abspath('conf'))
import settings

class HadoopBugDetector:
    def __init__(self, file_path, jiraLoader):
        self.jiraLoader = jiraLoader
        self.logger = Logger(__name__)
        self.matchedJira = []

        if not os.path.isfile(file_path):
            self.logger.error("File: %s does not exist", file_path)
            return

        self.file_path = file_path
        self.match_pattern = ".*Caused by.*"

    def detect(self):
        self.logger.info("Extracting file: %s", self.file_path)

        line_count = Utils.line_count_wc(self.file_path)
        self.logger.info("Total lines found: " + str(line_count) + " on file " + self.file_path)

        progress = int(line_count * settings.PROGRESS_PERCENTAGE)
        self.logger.info("Will print progress every " + str(progress) + " lines")

        line_num = 0
        with open(self.file_path, 'r') as f:
            for line in f:
                line_num += 1
                line = line.strip()
                if line.find('Caused by') >= 0: #re.search(self.match_pattern, line):
                    self.logger.debug("Found line: %s at line %d", line, line_num)
                    self.detect2(line, line_num)

                if line_num >= progress and line_num % progress == 0:
                    self.logger.info("Reading: " + str(
                        "{0:.2f}".format(float(line_num) / line_count * 100)) + "% on file " + self.file_path)

        self.logger.info("Finished extracting file: %s", self.file_path)

    def detect2(self, line, line_num):
        for jiraID in self.jiraLoader.lines:
            for l in self.jiraLoader.lines[jiraID]:
                ratio = SequenceMatcher(None, line, l).ratio()
                if ratio >= settings.SIMILARITY_RATIO:
                    self.logger.info("")
                    self.logger.info("Similarity ratio: %s found in JIRA %s", str(ratio), jiraID)
                    self.logger.info("JIRA line: %s", l)
                    self.logger.info("File line: %s at %d", line, line_num)

                    self.matchedJira.append(jiraID)
                    return
