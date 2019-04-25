from indicator.indicator import Indicator
from pms7003.pms7003 import Pms7003Sensor

led = Indicator()
sensor = Pms7003Sensor('/dev/serial0')

led.fill_dim()

while True:
    values = sensor.read()
    print(values)
    led.set(round(values['pm2_5']/24*100))