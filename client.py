import time
from infrastructure.config import *
from pms7003.threaded import Pms7003ThreadedReader
from requester import RequestDaemon



data_sender = RequestDaemon(MEASUREMENTS_URI)
data_sender.start()


with Pms7003ThreadedReader(serial_device=PMS_DEV, bufsize=PMS_BUF_SIZE) as pms_reader:
    
    #let PMS sensor collect some values
    time.sleep(2) #TODO: change it for sth less brittle
    
    seq = 0
    while True:
        
        data_dict = pms_reader.filtered_values()

        logging.info("received from PMS sensor {}".format(data_dict))
        data_sender.feed_data(data_dict)
        seq+=1
        time.sleep(1)
