
from machine import Pin, SoftI2C
from . import sht31
from BaseInterfaces.singleton import Singleton


class TempHumiditySensor(Singleton):
    def init(self, sda_pin, scl_pin, address, freq=400000):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq)
        sensor = sht31.SHT31(i2c, addr=address)

        self.i2c = i2c
        self.sensor = sensor

    def read_temp_humidity(self):
        return self.sensor.get_temp_humi()
