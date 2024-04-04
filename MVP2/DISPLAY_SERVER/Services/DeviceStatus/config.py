from BaseInterfaces.config import Config
from main_config import MainConfig


class DeviceStatusServiceConfig(Config):
    name = "DeviceStatusService"
    source_name = f"{MainConfig.device_name}"
