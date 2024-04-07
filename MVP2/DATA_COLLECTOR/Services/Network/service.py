from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Logger.service import LoggerService
from time import sleep
import json

import network
import urequests


class NetworkService(Service, Singleton):

    def init(self, name, source_name, ssid, password, request_timeout, max_try=3):
        self.name = name
        self.source_name = source_name

        self.ssid = ssid
        self.password = password
        self.max_try = max_try
        self.request_timeout = request_timeout

        self.station = network.WLAN(network.STA_IF)
        self.station.active(True)

        self.loggerService = LoggerService()

    def loop(self):
        try:
            self.connect()
        except Exception as e:
            print("ERROR wifi connect", e)

    def is_connected(self):
        return self.station is not None and self.station.isconnected()

    def connect(self):
        self.loggerService.log(f"{self.ssid}: {"connected" if self.is_connected() else "not connected"}")

        if self.is_connected():
            return

        sleep(1)
        self.station.connect(self.ssid, self.password)

        for i in range(10):
            sleep(1)
            print(f"[{i}] wait to connect wifi")
            if self.is_connected():
                return

    def wait_for_connection(self):
        try_count = 0
        while not self.is_connected():
            sleep(1)

            try_count += 1
            if try_count == self.max_try:
                return False

        return True

    def post_request(self, url, data):

        if not self.is_connected():
            return -1, None

        try:
            response = urequests.post(
                url, json=data, timeout=self.request_timeout)
            return response.status_code, response.text
        except Exception as e:
            print("ERROR POST:", e)
            return -1, None
