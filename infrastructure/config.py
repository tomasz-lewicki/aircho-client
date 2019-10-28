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
MEASUREMENTS_URI = 'http://10.0.0.124:5000/nodes/1/measurements/'

#PBay config
PBAY_EN=False
PBAY_DEV='/dev/ttyUSB0'

#pms7003 config
PMS_DEV='/dev/serial0'
PMS_BUF_SIZE=300 #that is about 5 minutes



#EXCEPTIONS/LOGGING
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("{} Uncaught exception".format(round(time.time())), exc_info=(exc_type, exc_value, exc_traceback))

if not DEBUG:
    sys.excepthook = handle_exception

logging.basicConfig(filename=LOG_PATH, level='INFO')
