import glob
import os, sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from Logger import Logger

class ApacheJiraLoader:
    def __init__(self):
        self.lines = {}
        logger = Logger(__name__)

        files = glob.glob("data/*")

        for file in files:
            logger.info("Loading JIRA: " + file)
            self.lines[file] = []
            with open(file, 'r') as f:
                lines = []
                for line in f:
                    lines.append(line.strip())

                self.lines[file] = lines
                logger.info("JIRA: " + file + " loaded with " + str(len(lines)) + " lines")
        
