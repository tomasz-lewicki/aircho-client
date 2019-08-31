import time
from infrastructure.config import *
from pms7003.threaded import Pms7003ThreadedReader
from pbay import PBay, Gas
from requester import RequestDaemon
from indicator import Indicator


data_sender = RequestDaemon(MEASUREMENTS_URI)
data_sender.start()

led = Indicator(1)
led.fill()
time.sleep(1)
led.fill_dim()
time.sleep(1)


gas_list = [
    Gas(name='CMO', calib_curr=9851, calib_temp=29.20, nanoamps_per_ppm=4.75, t_const=12, temp_source='AT0'),
    Gas(name='H2S', calib_curr=0, calib_temp=30, nanoamps_per_ppm=212, t_const=13, temp_source='AT3'),
    Gas(name='SO2', calib_curr=0, calib_temp=30, nanoamps_per_ppm=25, t_const=14, temp_source='AT3'),
    Gas(name='IAQ', calib_curr=0, calib_temp=30, nanoamps_per_ppm=30, t_const=12, temp_source='AT1'),
    Gas(name='IRR', calib_curr=0, calib_temp=30, nanoamps_per_ppm=50, t_const=17, temp_source='AT1'),
    Gas(name='NO2', calib_curr=0, calib_temp=30, nanoamps_per_ppm=30, t_const=50, temp_source='AT2'),
    Gas(name='OZO', calib_curr=0, calib_temp=30, nanoamps_per_ppm=30, t_const=50, temp_source='AT2'),
    ]



with Pms7003ThreadedReader(serial_device=PMS_DEV, bufsize=PMS_BUF_SIZE) as pms_reader,
    PBay(serial_address=devname, log_filename='log.txt', gas_list=gas_list) as sensor::
    
    #let PMS sensor collect some values
    time.sleep(2) #TODO: change it for sth less brittle

    seq = 0
    while sensor._is_running:
        
        pms_data_dict = pms_reader.filtered_values()

        logging.info("received from PMS sensor {}".format(pms_data_dict))

        led.set(int(pms_data_dict['pm10']/25*100))

        print(sensor.CMO)
        print(sensor.SO2)
        print(sensor.OZO)

        #only send a request every 60s
        if not seq % 60: data_sender.feed_data(pms_data_dict)
        seq+=1
        time.sleep(1)
