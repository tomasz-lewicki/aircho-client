import time
import os
import sys
import logging 
import serial.threaded
from pms7003.Pms7003ThreadedReader import Pms7003ThreadedReader
from pbay.pbay import PBayParser
from RequestDaemon import RequestDaemon


#TODO: put it in a config file
LOG_PATH = os.environ['LOG_PATH']
URI = os.environ['URI']
NODE_ID = os.environ['NODE_ID']
PBAY_DEV = os.environ['PBAY_DEV']
PMS_DEV = os.environ['PMS_DEV']
PMS_BUF_SIZE = int(os.environ['PMS_BUF_SIZE'])
MEASUREMENTS_URI = URI + NODE_ID

#EXCEPTIONS/LOGGING
def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("{} Uncaught exception".format(round(time.time())), exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
logging.basicConfig(filename=LOG_PATH, level='INFO')
#END OF EXCEPTIONS/LOGGING


#PERIPHERALS CONFIG

#TODO: make it Pms-style reader
serial_pbay = serial.Serial(port=PBAY_DEV, baudrate=115200, timeout=1)

pms_reader = Pms7003ThreadedReader(serial_device=PMS_DEV, bufsize=PMS_BUF_SIZE)
pms_reader.start()
time.sleep(2) #let PMS sensor collect some values #TODO: change it for sth less brittle

data_sender = RequestDaemon(MEASUREMENTS_URI)
data_sender.start()

with serial.threaded.ReaderThread(serial_pbay, PBayParser) as reader:
    while True:
        #print('H2S', reader.values['H2S'], 'SO2', reader.values['SO2'], 'NO2', reader.values['NO2'], 'OZO: ' ,reader.values['OZO'])
        pms_data_dict = pms_reader.filtered_values()
        data_sender.feed_data(pms_data_dict)
        
        time.sleep(1)