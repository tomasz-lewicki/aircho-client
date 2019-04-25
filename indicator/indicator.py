import board
import neopixel
import time
import math


class Indicator:
    def __init__(self, brightness=1):

        self.pixel_count = 24

        red_step = 255/(self.pixel_count)
        green_step = 1.5*255/(self.pixel_count)


        self.colormap = [(int(i * red_step), max(0,255-int(i * green_step)) ,0,0) for i in range(0, self.pixel_count)]
        dim_factor = 5
        self.colormap_dim = list(map(lambda a: (int(a[0]/dim_factor), int(a[1]/dim_factor), int(a[2]/dim_factor), int(a[3]/dim_factor)), self.colormap))
        self.pixels = neopixel.NeoPixel(board.D18, self.pixel_count, brightness=brightness, auto_write=True, pixel_order=neopixel.GRBW)

    def fill(self):
        for idx, color in enumerate(self.colormap):

            self.pixels[idx] = color
            time.sleep(0.03)
    
    def clear(self):
        for i in range(0, self.pixel_count): # clear all the pixels
            self.pixels[i] = (0,0,0,0)
            time.sleep(0.03)

    def fill_dim(self):
        for idx, color in enumerate(self.colormap):

            self.pixels[idx] = self.colormap_dim[idx]
            time.sleep(0.03)

    def set(self, percentage):        
        percentage = max(min(percentage, 100),0)
        tick_idx = round(percentage/100 * (self.pixel_count-1))
        print(percentage)
        print(tick_idx)
        print("percentage", percentage)
        pixel_value = round(percentage/100 * 255)

        self.pixels[tick_idx] = (0,0,0,0)
        time.sleep(0.5)
        self.pixels[tick_idx] = self.colormap[tick_idx]
        time.sleep(0.1)


if __name__ == '__main__':

    led = Indicator(1)
    
    led.fill()
    time.sleep(1)
    led.fill_dim()
    time.sleep(1)

    led.set(50)