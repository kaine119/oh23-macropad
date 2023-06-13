# Extension class to query VL53L0 ToF distance sensor 
# and do stuff based on values.

from kmk.extensions import Extension
import board
import neopixel
from adafruit_fancyled.adafruit_fancyled import CHSV
import busio
import math

import adafruit_vl53l0x

pixels = neopixel.NeoPixel(board.GP12, 1)
i2c = busio.I2C(board.GP7, board.GP6)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

class MyExtension(Extension):
    def after_hid_send(self, keyboard):
        # print(sensor.range)
        brightness = 255 - math.floor(sensor.range / 300 * 255)
        print(brightness)
        colour = CHSV(0, 255, brightness)
        pixels[0] = colour.pack()
        pixels.show()
        return
        
    def on_runtime_enable(self, keyboard):
        return

    def on_runtime_disable(self, keyboard):
        return

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        '''
        Return value will be injected as an extra matrix update
        '''
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def deinit(self, keyboard):
        pass