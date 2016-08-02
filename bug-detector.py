import os, sys
from lib.HadoopBugDetector import HadoopBugDetector
from lib.ApacheJiraLoader import ApacheJiraLoader
from lib.Logger import Logger

logger = Logger(__name__)

supported_types = ["hive", "impala", "hdfs", "hbase"]
help_text = "Run command as:\n\n" \
            "python bug-detector.py <log_filename> <type>\n" \
            "where <type> is one of the following: " + ", ".join(supported_types) + "\n"

if len(sys.argv) != 3:
    print "Expecting exactly two parameters\n"
    print help_text
    exit(1)

filename = sys.argv[1]
type = sys.argv[2]

if not os.path.isfile(filename):
    logger.error("File: %s does not exist", filename)
    exit(1)

detector = HadoopBugDetector(filename, ApacheJiraLoader(type))
detector.detect()

if len(detector.matchedJira) > 0:
    print "\n".join(detector.matchedJira)
else:
    print "No bugs detected"
