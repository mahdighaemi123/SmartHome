from BaseInterfaces.config import Config
from main_config import MainConfig

class DisplayServerServiceConfig(Config):
    name = "DisplayServerService"
    source_name = f"{MainConfig.device_name}"
