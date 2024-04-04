from time import sleep

from Services.Display.service import DisplayService
from Services.Display.config import DisplayServiceConfig

from Services.Logger.service import LoggerService
from Services.Logger.config import LoggerServiceConfig

from Services.Network.service import NetworkService
from Services.Network.config import NetworkServiceConfig

from Services.Getway.service import GetwayService
from Services.Getway.config import GetwayServiceConfig

from Services.Server.service import ServerService
from Services.Server.config import ServerServiceConfig

from Services.Display.service import DisplayService
from Services.Display.config import DisplayServiceConfig

from Services.DisplayServer.service import DisplayServerService
from Services.DisplayServer.config import DisplayServerServiceConfig

from Services.DeviceStatus.service import DeviceStatusService
from Services.DeviceStatus.config import DeviceStatusServiceConfig


services = []


def register_service(**keywords):
    services.append(
        keywords
    )


def register_services():

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
        service=ServerService,
        config=ServerServiceConfig
    )

    register_service(
        service=DisplayService,
        config=DisplayServiceConfig
    )

    register_service(
        service=DisplayServerService,
        config=DisplayServerServiceConfig
    )

    register_service(
        service=DeviceStatusService,
        config=DeviceStatusServiceConfig
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

            sleep(0.1)


def main():
    register_services()
    init_services()
    loop_services()


main()
