from BaseInterfaces.config import Config
from main_config import MainConfig


class LoggerServiceConfig(Config):
    name = "LoggerService"
    source_name = f"{MainConfig.device_name}"
    save_max_log = 3
    display_max_log = 3
