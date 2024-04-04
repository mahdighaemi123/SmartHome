# SmartHome - MVP 2
Minimume version of smart home
- Provide temp, humidity, rain status, light intensity from sesores and rain status prediction for tomorow
- Save readed datas to database
- Monitor datas on LCD

## How its work
We have three main-part with micro-service architecture
1. Server
2. Data collector
3. Display server

#### 1.Server services:
- mongo: mongodb container
- datakeeper: keeper of all datas
- getway: a centeral unit act as connector between serviced
- light_intensity_keeper: store and retrive light intensity
- temp_keeper: store and retrive temp 
- humidity_keeper: store and retrive humidity 
- rain_status_keeper: store and retrive rain status
- light_intensity_keeper: store and retrive light intensity
- device_status_keeper: store and retrive device status
- date_time_server: provide date and time
- rain_prediction_server: predict rain status
- monitor: read all statuses and display it on display server

#### 2.Data collector services:
- device_status: send device status to server
- display: internal service for display on oled
- getway: interface servive for connecting to server services
- light_intensity: service for handeling light intensity data
- rain_status: service for handeling rain status data
- temp_and_humidity: service for handeling temp and humidity data
- logger: internal logger service
- network: wifi connector service
- server: small http server provider
 
#### 3.Display server services:
- device_status: send device status to server
- display: internal service for display on lcd
- display_server: server for recive data and display them
- getway: interface servive for connecting to server services
- logger: internal logger service
- network: wifi connector service
- server: small http server provider 

## Stack
- Python for server
- MicroPython for IoT

## Sensors
- Rainfall sensor -> raining(True,False)
- SHT31 Temp and humidity sensor -> temp(float), humidity(float)
- BH1750 -> light_intensity(float)

## Displays
- OLED -> 128*32
- LCD -> 20*04

## Devices
- ESP32 -> Data collector, Display server
- HP Server -> Server
- Mi4c -> Router


 

## Setup
1. Setup display server
2. Setup data collector
3. Setup server

### 1. Setup display server
1. Edit config.py in DISPLAY_SERVER/Network/config.py:
```
class NetworkServiceConfig(Config):
    ssid = "<YOUR_WIFI_PASSWORD>"
    password = "<YOUR_WIFI_PASSWORD>"
```

2. Edit config.py in DISPLAY_SERVER/Getway/config.py:
```
class GetwayServiceConfig(Config):
    getway_url = "http://<YOUR_SERVER_IP | DOMAIN>:6001"
```

3. Flash Micropython fireware to your ESP32 | ESP1866
4. Transfer DataCollector directory files to your ESP (You can use Pymakr in vscode)
5. Turn on your wifi
6. Power on your esp

 
### 2. Setup data collector
1. Edit config.py in DATA_COLLECTOR/Network/config.py:
```
class NetworkServiceConfig(Config):
    ssid = "<YOUR_WIFI_PASSWORD>"
    password = "<YOUR_WIFI_PASSWORD>"
```

2. Edit config.py in DATA_COLLECTOR/Getway/config.py:
```
class GetwayServiceConfig(Config):
    getway_url = "http://<YOUR_SERVER_IP>:6001"
```

2. Flash Micropython fireware to your ESP32 | ESP1866
3. Transfer DataCollector directory files to your ESP (You can use Pymakr in vscode)
4. Turn on your wifi
5. Power on your esp


### 3. Setup server
1. Edit `docker-compose.yaml`
```
services:
  services_getway:
    environment
      DisplayServer: http://<DISPLAY_SERVER_IP>:8080
```

2. Start with docker compose in server directory
```
docker compose up
```

It starts all server services as containers