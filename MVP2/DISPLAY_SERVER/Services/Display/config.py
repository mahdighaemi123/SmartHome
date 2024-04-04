from BaseInterfaces.config import Config
from main_config import MainConfig

class DisplayServiceConfig(Config):
    name = "DisplayService"
    source_name = f"{MainConfig.device_name}"

    scl_pin = 22
    sda_pin = 21
    i2c_addr = 0x27
    num_rows = 4
    num_cols = 20
    freq = 800000
