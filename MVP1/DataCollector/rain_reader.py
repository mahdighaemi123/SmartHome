
from machine import Pin
import libs.ssd1306 as ssd1306

class RainReader:
    def __init__(self,pin):
        self.digital_pin = Pin(pin, Pin.IN)

    def read(self):
        digital_value = self.digital_pin.value()
        is_raining = digital_value == 0
        return is_raining
