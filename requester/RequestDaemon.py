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
            time.sleep(1)
            if self._new_data:
                request_fields = {}
                request_fields['timestamp'] = time.time()
                request_fields['values'] = self._data_dict
                
                r=requests.post(self._URI, headers={'Content-Type': 'application/json'}, json=request_fields, timeout=4)

                if r.status_code == 201:
                    logging.info("Request success @ {} {} {} {}".format(time.time(), r.status_code, r.text, request_fields))
                    self._new_data = False
                else:
                    logging.error("Error @ {} {} {} {}".format(time.time(), r.status_code, r.text, request_fields))
                del r # had some problems with hanging requests causing memory leaks. There's probably a better way... 

            else:
                time.sleep(1)

    def feed_data(self, data_dict):
        self._new_data = True
        self._data_dict = data_dict

