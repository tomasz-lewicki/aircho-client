import time
from infrastructure.config import *
from pms7003.threaded import Pms7003ThreadedReader
from pbay import PBayThreadedReader
from requester import RequestDaemon
from indicator import Indicator


data_sender = RequestDaemon(MEASUREMENTS_URI)
data_sender.start()

led = Indicator(1)
led.fill()
time.sleep(1)
led.fill_dim()
time.sleep(1)

if PBAY_EN:
    while True:
        time.sleep(1)
        # with PBayThreadedReader('/dev/ttyUSB0') as pbay_reader, Pms7003ThreadedReader(serial_device=PMS_DEV, bufsize=PMS_BUF_SIZE) as pms_reader:
        #     #let PMS sensor collect some values
        #     time.sleep(2) #TODO: change it for sth less brittle

        #     i = 0
        #     while True:
                
        #         pms_data_dict = pms_reader.filtered_values()
        #         pbay_data_dict = pbay_reader.values

        #         print(pbay_data_dict)
        #         print(pms_data_dict)

        #         led.set(int(pms_data_dict['pm10']/25*100))

        #         data_sender.feed_data(pms_data_dict)
        #         time.sleep(1)

else:
    with Pms7003ThreadedReader(serial_device=PMS_DEV, bufsize=PMS_BUF_SIZE) as pms_reader:
        #let PMS sensor collect some values
        time.sleep(2) #TODO: change it for sth less brittle

        i = 0
        while True:
            
            pms_data_dict = pms_reader.filtered_values()

            logging.info(time.time(),pms_data_dict)

            led.set(int(pms_data_dict['pm10']/25*100))

            data_sender.feed_data(pms_data_dict)
            time.sleep(1)