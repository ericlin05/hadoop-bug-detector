import os, sys
from lib.HadoopBugDetector import HadoopBugDetector
from lib.ApacheJiraLoader import ApacheJiraLoader
from lib.Logger import Logger

filename = sys.argv[1]
logger = Logger(__name__)

if not os.path.isfile(filename):
    logger.error("File: %s does not exist", filename)
    exit(1)

detector = HadoopBugDetector(filename, ApacheJiraLoader())
detector.detect()

print detector.matchedJira