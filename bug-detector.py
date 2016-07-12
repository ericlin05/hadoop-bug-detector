import os, sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from HadoopBugDetector import HadoopBugDetector
from ApacheJiraLoader import ApacheJiraLoader
from Logger import Logger

jiraLoader = ApacheJiraLoader()

filename = sys.argv[1]

logger = Logger(__name__)

if not os.path.isfile(filename):
    logger.error("File: " + filename + " does not exist")
    exit(1)

detector = HadoopBugDetector(filename, jiraLoader)
detector.detect()
