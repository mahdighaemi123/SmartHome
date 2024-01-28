# SmartHome - MVP 1
Minimume version of smart home
- Provide temp, humidity, rain_status for display
- Save readed datas to database

## How its work
### Stage1 - Data reader
1. Read temp, humidity ,rain_status 
2. Display on OLED
3. Send data with rest api call to server
 
### Stage2 - Server 
3. Recive data from Data reader 
4. Save data on db

## Stack
- Python for server
- MicroPython for clients

## Sensors
- Rain sensor -> raining(True,False)
- SHT31 Temp and humidity sensor -> temp(float), humidity(float)

## Displays
- OLED -> show rain, temp ,humidity

## Devices
- ESP32 -> Data reader
- HP Server -> Server
- Mi4c -> Router

## Display format
- OLED -> show rain, temp, humidity
Wheather: Raining | NoRain
Temp       : 52.30°
Humidity  : 20.70%

## Database
temp, humidity, rain_status, timestamp

## Setup

### - Setup server
Start with docker compose in server folder
```
docker compose up
```

It starts 
- api cintainer
- mongodb cintainer

Using ports
1. api use 5000 port
2. mongodb use 27017 port

### - Setup data collector
1. Creat config.py file in DataCollector folder with:
```
config = {
    "name":"DARA_COLLECTOR_1",
    "server_url":"http://<YourServerIp>:5000/new_data",
    "wifi_ssid":"<YourWifiSSID>",
    "wifi_password":"<YourWifiPassword>",
    "interval":60,
    "raining_sensor_pin":13,
    "display_scl_pin":22,
    "display_sda_pin":21,
    "display_width":128,
    "display_height":32,
    "display_line_height":12,
    "temphumidity_sensor_sda":4,
    "temphumidity_sensor_scl":5,
    "temphumidity_sensor_address":0x44,
}
```

2. Flash Micropython fireware to your ESP32 | ESP1866
3. Transfer DataCollector folder files to your ESP (You can use Pymakr in vscode)
4. Turn on your wifi
5. Power on your esp