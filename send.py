import requests
import json
import time

#from requests import ConnectionError
from pms7003.pms7003 import Pms7003Sensor, PmsSensorExcpetion

if __name__ == '__main__':

    sensor = Pms7003Sensor('/dev/serial0')
    j = {}

    while True:
        try:
            j['values'] = sensor.read()
        except PmsSensorExcpetion:
            print('Connection problem') 
        
        j['timestamp'] = time.time()

        try:
            r=requests.post('https://smog-monitor.herokuapp.com/api/get-one', json=json.dumps(j))
            print(r.status_code)
            if r.status_code != 200:
                time.sleep(1)
        except ConnectionError:
            print('Network connection problem')




            


# if __name__ == '__main__':
    
# 	dump=json.dumps(list_of_tuples)
	
# 	try:
# 		r=requests.post('http://46.101.98.211/hehe/1234',json=dump)
# 		list_of_tuples=[]
# 		logging.info('batch succeded with code:'.format(r.status_code))
		
# 	except (requests.exceptions.ConnectionError, ConnectionRefusedError) as e:
# 		logging.error('batch failed with error:'.format(e))
	
# 	return list_of_tuples
