
import os
from monitor import Monitor
from services_getway import ServicesGetway
from display_server import DisplayServer

import pprint
import time

connection_string = os.environ.get(
    "GETWAY", "http://127.0.0.1:6001/")

getway = ServicesGetway(connection_string)

monitor = Monitor(
    getway=getway,
)

displayServer = DisplayServer(
    getway=getway,
)

while True:

    try:
        status = monitor.get_status()
        pprint.pprint(status)
        print()

        lines = list()
        lines.append(
            f'Time:{status["date_time"]["hour"]}:{status["date_time"]["minute"]}:{status["date_time"]["second"]} {status["date_time"]["jweek_day_en_short"]}')

        lines.append(
            f'Date:{status["date_time"]["jyear"]}/{status["date_time"]["jmonth"]}/{status["date_time"]["jday"]} {status["date_time"]["jmonth_en"]}')

        lines.append(
            f'Temp:{round(status["temp"])}C Humi:{round(status["humidity"])}%')

        lines.append(f'Rain:{"Now" if status["rain_status"] else ""}{"," if status["tomorrow_rain_status_prediction"] and status["rain_status"] else ""}{"24h" if status["tomorrow_rain_status_prediction"] else ""}{"No-Rain" if not status["tomorrow_rain_status_prediction"] and not status["rain_status"] else ""} Sun:{str(status["light_intensity"]//1000)+"K" if status["light_intensity"] >= 1000 else round(status["light_intensity"])}')

        displayServer.display(lines=lines)

    except Exception as e:
        print("ERROR", e)

    time.sleep(0.720)
