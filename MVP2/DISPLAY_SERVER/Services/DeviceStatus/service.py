from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton
from Services.Getway.service import GetwayService
from Services.Logger.service import LoggerService


class DeviceStatusService(Service, Singleton):
    def init(self, name, source_name):
        self.name = name
        self.source_name = source_name

        self.getwayService = GetwayService()
        self.loggerService = LoggerService()

    def register_device_status(self, device_status):

        data = {
            "source_name": self.source_name,
            "service_name": self.name,
            "device_status": device_status
        }

        result = self.getwayService.service_call(
            service_name="DeviceStatusKeeper",
            endpoint="/device_status/register",
            data=data
        )

        return result

    def loop(self):
        device_status = "GOOD"

        self.loggerService.log(f"DeviceStatus: {device_status}")

        self.register_device_status(device_status=device_status)
