import os
import os
import sys
import logging 
import time

LOG_PATH = os.environ['LOG_PATH']
URI = os.environ['URI']
NODE_ID = os.environ['NODE_ID']
PBAY_DEV = os.environ['PBAY_DEV']
PMS_DEV = os.environ['PMS_DEV']
DEBUG = os.environ['DEBUG']
PMS_BUF_SIZE = int(os.environ['PMS_BUF_SIZE'])
MEASUREMENTS_URI = URI + NODE_ID

#EXCEPTIONS/LOGGING
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("{} Uncaught exception".format(round(time.time())), exc_info=(exc_type, exc_value, exc_traceback))

if not DEBUG:
    sys.excepthook = handle_exception

logging.basicConfig(filename=LOG_PATH, level='INFO')