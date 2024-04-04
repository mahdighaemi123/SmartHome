from BaseInterfaces.config import Config
from main_config import MainConfig


class DisplayerServiceConfig(Config):
    name = "DisplayerService"
    source_name = f"{MainConfig.device_name}"

    scl_pin = 22
    sda_pin = 21
    width = 128
    height = 32
    line_height = 12
