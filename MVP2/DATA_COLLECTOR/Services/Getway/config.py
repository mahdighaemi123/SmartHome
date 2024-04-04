from BaseInterfaces.config import Config
from main_config import MainConfig


class GetwayServiceConfig(Config):
    name = "GetwayService"
    source_name = f"{MainConfig.device_name}"
    getway_url = "http://192.168.31.134:6001"
    getway_service_call_endpoint = "/services/call"
 