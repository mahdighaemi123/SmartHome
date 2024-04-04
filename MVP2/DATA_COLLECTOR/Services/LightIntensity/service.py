from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Logger.service import LoggerService
from Services.Getway.service import GetwayService

from .Interfaces.light_intensity_sensor import LightIntensitySensor


class LightIntensityService(Service, Singleton):

    def init(self, name, source_name, scl_pin, sda_pin):
        self.name = name
        self.source_name = source_name
        self.lightIntensitySensor = LightIntensitySensor(
            scl_pin=scl_pin, sda_pin=sda_pin)

        self.loggerService = LoggerService()
        self.getwayService = GetwayService()

    def register_light_intensity(self, light_intensity):

        data = {
            "source_name": self.source_name,
            "service_name": self.name,
            "light_intensity": light_intensity
        }

        result = self.getwayService.service_call(
            service_name="LightIntensityKeeper",
            endpoint="/light_intensity/register",
            data=data
        )

        return result

    def loop(self):
        light_intensity = self.lightIntensitySensor.measure_light()

        self.loggerService.log(f"LightIntensity: {light_intensity}")

        self.register_light_intensity(light_intensity=light_intensity)
