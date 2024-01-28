from time import sleep
import json

import urequests
import network

class NetworkHandler():

    def __init__(self,ssid,password,max_try=3):
        self.ssid = ssid
        self.password = password
        self.max_try = max_try
        self.station = None

    def connect(self):
        if self.is_connected():
            return
        
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(self.ssid, self.password)
        self.station = station

    def is_connected(self):
        return self.station is not None and self.station.isconnected()
    
    def wait_for_connection(self):
        try_count = 0
        while not self.is_connected():
            sleep(1)

            try_count+=1
            if try_count == self.max_try:
                return False
            
        return True

    def post_data(self, url, data):
        response = urequests.post(url,json=data)
        # response.close()
        return response.status_code, response.text

