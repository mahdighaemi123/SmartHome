from BaseInterfaces.config import Config
from main_config import MainConfig

class ServerServiceConfig(Config):
    name = "ServerService"
    source_name = f"{MainConfig.device_name}"

    port = 8080
    host = "0.0.0.0"