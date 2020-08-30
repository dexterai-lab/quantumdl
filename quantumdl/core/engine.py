from quantumdl.core.engine import *
import logging

# create logger for the current application
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

class QDLengine:
    """This class provides the core functionality for Quantum Deep Learning Engine"""

    def __init__(self, **kwargs):
        self.__name__

def main():
    """This is the main function"""
    pass

if __name__ == '__main__':
    main()
