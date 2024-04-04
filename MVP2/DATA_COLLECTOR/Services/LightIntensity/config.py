from BaseInterfaces.config import Config
from main_config import MainConfig


class LightIntensityServiceConfig(Config):
    name = "LightIntensityService"
    source_name = f"{MainConfig.device_name}"
    scl_pin = 18
    sda_pin = 19
