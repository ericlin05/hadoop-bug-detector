import os, sys

lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)

from ApacheJiraParser import ApacheJiraParser

parser = ApacheJiraParser('SENTRY-893') 
parser.parse().write()
