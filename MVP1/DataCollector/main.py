
from time import sleep
from rain_reader import RainReader
from logger_tool import LoggerTool
from temp_humidity_reader import TempHumidityReader
from displayer import Displayer
from config import config
from network_handler import NetworkHandler

def main():
    loggerTool = LoggerTool()
    loggerTool.start_log()

    rainReader = RainReader(pin=config["raining_sensor_pin"])
    tempHumidityReader = TempHumidityReader(
        sda_pin=config["temphumidity_sensor_sda"],
        scl_pin=config["temphumidity_sensor_scl"],
        address=config["temphumidity_sensor_address"]
    )

    displayer = Displayer(
        scl_pin=config["display_scl_pin"],
        sda_pin=config["display_sda_pin"],
        width=config["display_width"],
        height=config["display_height"],
        line_height=config["display_line_height"]
    )

    networkHandler = NetworkHandler(ssid=config["wifi_ssid"],password=config["wifi_password"])

    while True:
        is_raining = rainReader.read()
        temp,humidity = tempHumidityReader.read()

        loggerTool.log(
            is_raining=is_raining,
            temp=temp,
            humidity=humidity
        )

        displayer.clear()
        displayer.display_line(f"Wheather:{('Raining' if is_raining else 'No Rain')}" ,0)
        displayer.display_line(f"Temp    :{temp:.2f}°",1)
        displayer.display_line(f"Humidity:{humidity:.2f}%",2)
        displayer.show()

        try:
            networkHandler.connect()
            if networkHandler.wait_for_connection():
                response_code, response_text = networkHandler.post_data(
                    url=config["server_url"],
                    data={
                        "name": config["name"],
                        "is_raining": is_raining,
                        "temp": temp,
                        "humidity": humidity
                    }
                )
                loggerTool.log_server_resp(config["server_url"],response_code, response_text)

        except Exception as e:
            print("NETWORK ERROR")
            print(e)

        sleep(config["interval"])


main()