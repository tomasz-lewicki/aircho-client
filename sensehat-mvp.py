import time
import aqi as aqi_converter # PM value to AQI converter

from pms7003.pms7003 import Pms7003Sensor, PmsSensorException
from sense_hat import SenseHat
from enum import Enum

# THRESHOLDS_PM2_5 = [
#     0,     # good
#     12.0,  # moderate
#     35.4,  # unhealthy for sensitive groups
#     55.4,  # unhealthy
#     150.4, # very unhealthy
#     250.4, # hazardous
#     350.4, # hazardous
#     ]
# ORANGE = (255, 165, 0)  # orange
# VERY_UNHEALTHY = (153, 51, 153)  # purple


class Colors(Enum):
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    orange = (255, 165, 0)
    red = (255, 0, 0)
    purple = (128, 0, 128)
    maroon = (128, 0, 0)


def aqi2color(aqi):
    if aqi < 50:
        return Colors.green.value
    elif aqi < 100:
        return Colors.yellow.value
    elif aqi < 150:
        return Colors.orange.value
    elif aqi < 200:
        return Colors.red.value
    elif aqi < 300:
        return Colors.purple.value
    else:
        return Colors.maroon.value


def fill_color(sense, color):
    """
    fill all pixels with color.
    color param is a tuple with 8-bit RGB color.
    For exaple: color=(255, 0, 0) for red
    """
    for row in range(8):
        for col in range(8):
            sense.set_pixel(row, col, color)


def readings2aqi(readings):
    aqi = aqi_converter.to_aqi(
        [
            (aqi_converter.POLLUTANT_PM25, readings["pm2_5"]),
            (aqi_converter.POLLUTANT_PM10, readings["pm10"]),
        ]
    )

    return aqi


if __name__ == "__main__":

    sensor = Pms7003Sensor("/dev/serial0")
    sense = SenseHat()

    while True:
        try:
            r = sensor.read()
            aqi = readings2aqi(r)
            c = aqi2color(aqi)
            fill_color(sense, c)
            print(r)
        except PmsSensorException:
            print("Connection problem")

    sensor.close()
