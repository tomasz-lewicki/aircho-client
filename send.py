import requests
import json
import time
import logging
import sys
from pms7003.pms7003 import Pms7003Sensor, PmsSensorExcpetion, VALUES

URI_PROD = 'https://aq-api.herokuapp.com/measurements/'
URI_DEVEL = 'http://192.168.1.66:5001/measurements/'
N_SAMPLES = 300 #around every 5mins

API_URI = URI_PROD

def handle_exception(exc_type, exc_value, exc_traceback):
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

def avg_n_readouts(n):
    c = {v: [] for v in VALUES }
    for _ in range(n):
        try:
            r = sensor.read()
            for v in VALUES:
                c[v].append(r[v]) #c is a dictionary of lists
        except PmsSensorExcpetion as e:
            logging.exception('{} {}'.format(int(1000*time.time()), e))
            break
    return {v: round((sum(c[v])/n), 2) for v in VALUES} #return a dict of averages

def send_request(j):
    try:
        r=requests.post(API_URI, json=json.dumps(j), timeout=4)
        logging.info('{} {}'.format(int(1000*time.time()), r.status_code))
        if r.status_code != 204:
            time.sleep(1)
        del r

    except requests.RequestException as e:
        logging.exception('{} {}'.format(int(1000*time.time()), e))

def mainloop():

    j={}
    a = avg_n_readouts(N_SAMPLES)
    j['values'] = a
    j['timestamp'] = time.time()
    send_request(j)

if __name__ == '__main__':

    time.sleep(5)
    sensor = Pms7003Sensor('/dev/serial0')
    sys.excepthook = handle_exception
    logging.basicConfig(filename='/home/pi/aq-sensor/aq-sensor.log', level='INFO')

    while True:
        mainloop()
