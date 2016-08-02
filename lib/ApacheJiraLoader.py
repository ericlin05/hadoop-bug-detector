import glob
from lib.Logger import Logger

class ApacheJiraLoader:
    def __init__(self, type):
        self.lines = {}
        logger = Logger(__name__)

        files = glob.glob("data/" + type.upper() + "/*")

        for file in files:
            logger.debug("Loading JIRA: " + file)
            self.lines[file] = []
            with open(file, 'r') as f:
                lines = []
                for line in f:
                    lines.append(line.strip())

                self.lines[file] = lines
                logger.debug("JIRA: %s loaded with %s lines", file, str(len(lines)))
        
