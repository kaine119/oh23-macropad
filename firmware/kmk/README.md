# KMK firmware for Macropad Workshop
Click the `.zip` and `.uf2` files above to download. 

After flashing the `.uf2`, unzip `circuitpy-contents` and copy the *contents* of the folder over, i.e. `code.py` should be at the top level of the `CIRCUITPY` drive.

## Code to copy
<details>
<summary>Import Libraries</summary>

```python
import board
import busio

import neopixel
from adafruit_fancyled.adafruit_fancyled import CHSV

import adafruit_vl53l0x

import math
```

</details>

<details>
<summary>Get values from the sensor</summary>

```python
# Under library imports:
i2c = busio.I2C(board.GP7, board.GP6)
sensor = adafruit_vl53l0x.VL53L0X(i2c)

# Under class MyKeyboard:
def after_hid_send(self, keyboard):
    # Just copy over the body of this function
    print(sensor.range)
```

</details>

<details>
<summary>Use the values to light up the LED</summary>

```python
i2c = busio.I2C(board.GP7, board.GP6)
sensor = adafruit_vl53l0x.VL53L0X(i2c)
pixels = neopixel.NeoPixel(board.GP12, 1)

def after_hid_send(self, keyboard):
    brightness = 255 - math.floor(sensor.range / 300 * 255)
    colour = CHSV(0, 255, brightness)
    pixels[0] = colour.pack()
    pixels.show()
```

</details>