import glob
from lib.Logger import Logger

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
                logger.info("JIRA: %s loaded with %s lines", file, str(len(lines)))
        