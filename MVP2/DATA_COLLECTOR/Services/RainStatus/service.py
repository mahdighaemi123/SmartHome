from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Logger.service import LoggerService
from Services.Getway.service import GetwayService

from .Interfaces.rain_status_sensor import RainStatusSensor

class RainStatusService(Service, Singleton):
    def init(self,name,source_name, sensor_digital_pin):
        self.name = name
        self.source_name = source_name

        self.rainStatusSensor = RainStatusSensor(
            sensor_digital_pin=sensor_digital_pin
        )

        self.loggerService = LoggerService()
        self.getwayService = GetwayService()

    def register_rain_status(self,rain_status):

        data = {
            "source_name": self.source_name,
            "service_name": self.name,
            "rain_status": rain_status
        }

        result = self.getwayService.service_call(
            service_name="RainStatusKeeper",
            endpoint="/rain_status/register",
            data=data
        )

        return result


    def loop(self):
        rain_status = self.rainStatusSensor.rain_status()

        self.loggerService.log(f"RainStatus: {"Raining" if rain_status else "No-rain"}")
        self.register_rain_status(rain_status=rain_status)

