
from machine import Pin, SoftI2C
import libs.sht31 as sht31

class TempHumidityReader():
    def __init__(self,sda_pin,scl_pin,address):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq =400000)
        sensor = sht31.SHT31(i2c, addr=address)

        self.i2c = i2c
        self.sensor = sensor

    def read(self):
        return self.sensor.get_temp_humi()
