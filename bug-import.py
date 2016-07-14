from lib.ApacheJiraParser import ApacheJiraParser

# for a in range(890,894):
#     parser = ApacheJiraParser('SENTRY-' + str(a))
#     parser.parse().write()

for a in range(8000,14240):
    parser = ApacheJiraParser('HIVE-' + str(a))
    parser.parse().write()
