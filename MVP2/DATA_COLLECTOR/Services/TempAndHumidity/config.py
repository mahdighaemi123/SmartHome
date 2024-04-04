from BaseInterfaces.config import Config
from main_config import MainConfig


class TempAndHumidityServiceConfig(Config):
    name = "TempAndHumidityService"
    source_name = f"{MainConfig.device_name}"
    sda_pin = 4
    scl_pin = 5
    address = 0x44
