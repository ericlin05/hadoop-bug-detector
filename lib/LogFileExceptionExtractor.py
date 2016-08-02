import glob, os, re
from lib.Logger import Logger

class LogFileExceptionExtractor:
    def __init__(self, file_path):
        self.logger = Logger(__name__)
        self.file_path = None
        self.new_file_path = None
        self.match_patterns = [
            ".*Caused by.*"
        ]

        if not os.path.isfile(file_path):
            self.logger.error("File: %s does not exist", file_path)
            return

        self.file_path = file_path
        self.new_file_path = file_path + ".extractor"

        self.line_count = self.line_count_wc(self.file_path)
        self.progress = int(self.line_count * .05)

        self.logger.info("Total lines found: " + str(self.line_count) + " on file " + self.file_path)
        self.logger.info("Will print progress every " + str(self.progress) + " lines")

    def extract(self):
        self.logger.info("Extracting file: %s", self.file_path)

        target = open(self.new_file_path, 'w')
        target.truncate()

        line_num = 0
        with open(self.file_path, 'r') as f:
            for line in f:
                line_num = line_num + 1
                if re.search("|".join(self.match_patterns), line):
                    target.write(line)

                if line_num >= self.progress and line_num % self.progress == 0:
                    self.logger.info("Reading: " + str("{0:.2f}".format(float(line_num) / self.line_count * 100)) + "% on file " + self.file_path)

        target.close()
        self.logger.info("Finished extracting file: %s", self.file_path)
        self.logger.info("Final extracted file contains : %d lines", self.line_count_wc(self.new_file_path))

    def remove(self):
        self.logger.info("Removing file: %s", self.new_file_path)
        os.remove(self.new_file_path)

    def line_count_wc(self, file_path):
        return int(os.popen('wc -l ' + file_path).read().split(  )[0])