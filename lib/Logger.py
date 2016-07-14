import logging

class Logger:
    def __init__(self, name):
        FORMAT = '[%(asctime)-15s] [%(levelname)s]: %(message)s'
        logging.basicConfig(format=FORMAT,level=logging.DEBUG,filename='log/test.log')
        self.logger = logging.getLogger(name)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)