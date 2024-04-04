
from machine import Pin
from BaseInterfaces.singleton import Singleton


class RainStatusSensor(Singleton):
    def init(self, sensor_digital_pin):
        self.pin = Pin(sensor_digital_pin, Pin.IN)

    def rain_status(self):
        digital_value = self.pin.value()
        rain_status = digital_value == 0
        return rain_status
