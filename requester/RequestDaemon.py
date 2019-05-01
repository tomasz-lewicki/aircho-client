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
                    request_fields['values'] = self._data_dict
                    request_fields['timestamp'] = time.time()
                    
                    h = {'Content-Type': 'application/json'}
                    j = json.dumps(request_fields)

                    print(self._URI)
                    print(j)
                    r=requests.post(self._URI, headers=h, json=j, timeout=4)

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

