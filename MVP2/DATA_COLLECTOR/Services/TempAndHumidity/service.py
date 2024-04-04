from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton
from Services.Logger.service import LoggerService
from Services.Getway.service import GetwayService
from .Interfaces.temp_humidity_sensor import TempHumiditySensor


class TempAndHumidityService(Service, Singleton):
    def init(self, name, source_name, sda_pin, scl_pin, address):
        self.name = name
        self.source_name = source_name

        self.tempHumiditySensor = TempHumiditySensor(
            sda_pin=sda_pin,
            scl_pin=scl_pin,
            address=address
        )

        self.loggerService = LoggerService()
        self.getwayService = GetwayService()

    def register_temp(self, temp):

        data = {
            "source_name": self.source_name,
            "service_name": self.name,
            "temp": temp
        }

        result = self.getwayService.service_call(
            service_name="TempKeeper",
            endpoint="/temp/register",
            data=data
        )

        return result

    def register_humidity(self, humidity):

        data = {
            "source_name": self.source_name,
            "service_name": self.name,
            "humidity": humidity
        }

        result = self.getwayService.service_call(
            service_name="HumidityKeeper",
            endpoint="/humidity/register",
            data=data
        )

        return result

    def loop(self):
        temp, humidity = self.tempHumiditySensor.read_temp_humidity()

        self.loggerService.log(f"Temp: {round(temp,2)}")
        self.loggerService.log(f"Humidity: {round(humidity,2)}")

        self.register_temp(temp=temp)
        self.register_humidity(humidity=humidity)
