import os

services = {
    "RainPredictionServer": {
        "address": os.environ.get("RainPredictionServer", "http://127.0.0.1:6002"),
        "method": "post"
    },
    "DataKeeper": {
        "address": os.environ.get("DataKeeper", "http://127.0.0.1:6003"),
        "method": "post"
    },
    "LightIntensityKeeper": {
        "address": os.environ.get("LightIntensityKeeper", "http://127.0.0.1:6004"),
        "method": "post"
    },
    "TempKeeper": {
        "address": os.environ.get("TempKeeper", "http://127.0.0.1:6005"),
        "method": "post"
    },
    "HumidityKeeper": {
        "address": os.environ.get("HumidityKeeper", "http://127.0.0.1:6006"),
        "method": "post"
    },
    "RainStatusKeeper": {
        "address": os.environ.get("RainStatusKeeper", "http://127.0.0.1:6007"),
        "method": "post"
    },
    "DeviceStatusKeeper": {
        "address": os.environ.get("DeviceStatusKeeper", "http://127.0.0.1:6008"),
        "method": "post"
    },
    "DateTimeServer": {
        "address": os.environ.get("DateTimeServer", "http://127.0.0.1:6009"),
        "method": "post"
    },
    "DisplayServer": {
        "address": os.environ.get("DisplayServer", "http://192.168.31.229:8080"),
        "method": "get"
    }
}
