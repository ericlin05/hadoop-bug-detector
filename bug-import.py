from lib.ApacheJiraParser import ApacheJiraParser
import pycurl
from lib.Logger import Logger

# for a in range(890,894):
#     parser = ApacheJiraParser('SENTRY-' + str(a))
#     parser.parse().write()

for a in range(9525,14240):
    parser = ApacheJiraParser('hive', a)

    logger = Logger(__name__)

    try:
        parser.parse().write()
    except pycurl.error as err:
        logger.error("Unable to parse JIRA: %s", 'HIVE-' + str(a))
        logger.error("Error: %s", str(err))
