from BaseInterfaces.config import Config
from main_config import MainConfig


class NetworkServiceConfig(Config):
    name = "NetworkService"
    source_name = f"{MainConfig.device_name}"
    ssid = "<YOUR_WIFI_PASSWORD>"
    password = "<YOUR_WIFI_PASSWORD>"
    max_try = 3
    request_timeout = 12
