import logging

class Logger:
    def __init__(self, name):
        FORMAT = '%(asctime)-15s: %(message)s'
        logging.basicConfig(format=FORMAT)
        self.logger = logging.getLogger(name)

    def info(self, s):
        self.logger.warning(s)


    def error(self, s):
        self.logger.error(s)