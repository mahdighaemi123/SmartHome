from BaseInterfaces.config import Config
from main_config import MainConfig


class RainStatusServiceConfig(Config):
    name = "RainStatusService"
    source_name = f"{MainConfig.device_name}"
    sensor_digital_pin = 13
