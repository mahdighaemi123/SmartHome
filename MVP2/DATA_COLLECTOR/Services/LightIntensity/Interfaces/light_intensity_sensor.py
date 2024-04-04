
from machine import I2C, Pin,SoftI2C
from BaseInterfaces.singleton import Singleton

from . import bh1750
from .sensor_pack.bus_service import I2cAdapter

import time


class LightIntensitySensor(Singleton):

    def init(self, scl_pin, sda_pin, freq=100000, measurement_accuracy=1):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq)
        self.adaptor = I2cAdapter(self.i2c)
        self.sol = bh1750.Bh1750(self.adaptor)

        self.sol.power(on=True)
        self.sol.set_mode(continuously=True, high_resolution=True)
        self.sol.measurement_accuracy = measurement_accuracy

    def measure_light(self):
        illumination = self.sol.get_illumination()
        time.sleep_ms(self.sol.get_conversion_cycle_time())
        return illumination
