import os, sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from ApacheJiraParser import ApacheJiraParser

for a in range(893,894):
    parser = ApacheJiraParser('SENTRY-' + str(a)) 
    parser.parse().write()

parser = ApacheJiraParser('HIVE-11084')
parser.parse().write()

