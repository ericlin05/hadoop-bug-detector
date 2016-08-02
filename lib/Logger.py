import logging, sys, os

sys.path.append(os.path.abspath('conf'))
import settings

class Logger:
    def __init__(self, name):
        FORMAT = '[%(asctime)-15s] [%(levelname)s]: %(message)s'
        logging.basicConfig(format=FORMAT,level=settings.LOG_LEVEL,filename='log/'+name+'.log')
        self.logger = logging.getLogger(name)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)