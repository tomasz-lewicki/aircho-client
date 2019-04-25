import board
import neopixel
import time

#pixels = neopixel.NeoPixel(board.D18, 24)

pixels = neopixel.NeoPixel(board.D18, 24, brightness=1, auto_write=True, pixel_order=neopixel.GRBW)


#pixels = 24 * [(0,0,0,0)]

for i in range(0,24):
    pixels[i] = (i*10, (24-i)*6, 0, 0)

'''four ranges
for i in range(0,6):
    pixels[i] = (0,i*40,0,0) 
    time.sleep(0.01)
    pixels.show()

for i in range(6,12):
    pixels[i] = (120,120,0,125)
    time.sleep(0.01)
    pixels.show()

for i in range(12,18):
    pixels[i] = (255,255,0,0)
    time.sleep(0.01)
    pixels.show()

for i in range(18,24):
    pixels[i] = (255,0,0,0)
    time.sleep(0.01)
    pixels.show()
'''

'''
for i in range(255):
    pixels.fill((0, 0, 0, i))
    time.sleep(0.01)
    pixels.show()

'''
