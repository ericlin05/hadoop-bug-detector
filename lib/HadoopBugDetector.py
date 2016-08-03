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

        # counts number of lines in the file, so that we can print out progress
        line_count = Utils.line_count_wc(self.file_path)
        self.logger.info("Total lines found: " + str(line_count) + " on file " + self.file_path)

        # determine when we print out progress information, based on settings.PROGRESS_PERCENTAGE
        progress = int(line_count * settings.PROGRESS_PERCENTAGE)
        self.logger.info("Will print progress every " + str(progress) + " lines")

        line_num = 0
        with open(self.file_path, 'r') as f:
            for line in f:
                line_num += 1
                line = line.strip()
                # only check for lines contains "Caused by" for now
                if line.find('Caused by') >= 0: #re.search(self.match_pattern, line):
                    self.logger.debug("Found line: %s at line %d", line, line_num)
                    self.find_similarity(line, line_num)

                # now prints the progress info
                if line_num >= progress and line_num % progress == 0:
                    self.logger.info("Reading: " + str(
                        "{0:.2f}".format(float(line_num) / line_count * 100)) + "% on file " + self.file_path)

        self.logger.info("Finished extracting file: %s", self.file_path)

    # this function scans through all JIRA files and check line by line to see if any line
    # that is very similar to the line passed, if the sequence matcher ratio is more than
    # the defined ratio, we will consider it as a match
    def find_similarity(self, line, line_num):
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
