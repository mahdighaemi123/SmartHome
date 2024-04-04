from time import sleep

from Services.Display.service import DisplayerService
from Services.Display.config import DisplayerServiceConfig

from Services.Logger.service import LoggerService
from Services.Logger.config import LoggerServiceConfig

from Services.Network.service import NetworkService
from Services.Network.config import NetworkServiceConfig

from Services.Getway.service import GetwayService
from Services.Getway.config import GetwayServiceConfig

from Services.DeviceStatus.service import DeviceStatusService
from Services.DeviceStatus.config import DeviceStatusServiceConfig

from Services.RainStatus.service import RainStatusService
from Services.RainStatus.config import RainStatusServiceConfig

from Services.TempAndHumidity.service import TempAndHumidityService
from Services.TempAndHumidity.config import TempAndHumidityServiceConfig

from Services.LightIntensity.service import LightIntensityService
from Services.LightIntensity.config import LightIntensityServiceConfig

services = []


def register_service(**keywords):
    services.append(
        keywords
    )


def register_services():

    register_service(
        service=DisplayerService,
        config=DisplayerServiceConfig
    )

    register_service(
        service=LoggerService,
        config=LoggerServiceConfig
    )

    register_service(
        service=NetworkService,
        config=NetworkServiceConfig
    )

    register_service(
        service=GetwayService,
        config=GetwayServiceConfig
    )
    
    register_service(
        service=DeviceStatusService,
        config=DeviceStatusServiceConfig
    )

    register_service(
        service=RainStatusService,
        config=RainStatusServiceConfig
    )

    register_service(
        service=TempAndHumidityService,
        config=TempAndHumidityServiceConfig
    )

    register_service(
        service=LightIntensityService,
        config=LightIntensityServiceConfig
    )


def init_service(service, config):
    service(**config.to_dict())


def init_services():
    for service in services:
        init_service(service["service"], service["config"])


def loop_service(service):
    service().loop()


def loop_services():
    while 1:
        for service in services:
            loop_service(service["service"])

            sleep(1)


def main():
    register_services()
    init_services()
    loop_services()


main()
