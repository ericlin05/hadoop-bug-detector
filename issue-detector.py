import os, sys
from lib.HadoopIssueDetector import HadoopIssueDetector
from lib.Logger import Logger

type = sys.argv[1]
filename = sys.argv[2]
logger = Logger(__name__)

if not os.path.isfile(filename):
    logger.error("File: %s does not exist", filename)
    exit(1)

detector = HadoopIssueDetector(type, filename)
detector.detect()

print detector.found