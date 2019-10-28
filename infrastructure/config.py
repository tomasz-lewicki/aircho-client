import os
import os
import sys
import logging 
import time

LOG_PATH = '/home/pi/logs'
URI = 'https://aircho-experimental.herokuapp.com/measurements/'
NODE_ID = '3'
DEBUG=False

#MEASUREMENTS_URI = URI + NODE_ID
MEASUREMENTS_URI = 'http://34.82.14.222/nodes/1/measurements/'
# MEASUREMENTS_URI = 'http://10.0.0.124/nodes/1/measurements/'

#PBay config
PBAY_EN=False
PBAY_DEV='/dev/ttyUSB0'

#pms7003 config
PMS_DEV='/dev/serial0'
PMS_BUF_SIZE=300 #that is about 5 minutes


# configure logger
logger = logging.getLogger('aircho_client')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler(LOG_PATH)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

#unhandled stuff
def handle_exception(exc_type, exc_value, exc_traceback):
    logger.error("{} Uncaught exception".format(round(time.time())), exc_info=(exc_type, exc_value, exc_traceback))
    exit(-1)
    
if not DEBUG:
    sys.excepthook = handle_exception