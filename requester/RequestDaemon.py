import requests
import threading
import json
import time
import logging
import sys


class RequestDaemon(threading.Thread):
    def __init__(self, URI):
        #TODO: feed logger in init
        super(RequestDaemon, self).__init__()
        self._URI = URI
        self._new_data = False

    def run(self):
        while True:
            if self._new_data:
                try:
                    request_fields = {}
                    request_fields['timestamp'] = time.time()
                    request_fields['values'] = self._data_dict
                    
                    r=requests.post(self._URI, headers={'Content-Type': 'application/json'}, json=request_fields, timeout=4)
                    print(r)

                    if r.status_code == 204:
                        logging.info('{} {}'.format(int(1000*time.time()), r.status_code))
                        self._new_data = False
                    else:
                        logging.error('{} {}'.format(int(1000*time.time()), r.status_code))
                    del r # had some problems with hanging requests causing memory leaks. There's probably a better way...
            
                except requests.RequestException as e:
                    logging.exception('{} {}'.format(int(1000*time.time()), e))
            else:
                time.sleep(1)

    def feed_data(self, data_dict):
        self._new_data = True
        self._data_dict = data_dict

