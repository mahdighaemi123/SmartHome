import requests


class HumidityKeeper():

    def __init__(self, getway):
        self.getway = getway

    def register_humidity(self, source_name, service_name, humidity, timestamp):

        data = {
            "source_name": source_name,
            "service_name": service_name,
            "timestamp": timestamp,
            "type": "humidity",
            "data": {
                "humidity": humidity
            }
        }

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/register",
            data={"data": data}
        )

        return result

    def retrive_last_humidity(self):

        query = {
            "type": "humidity"
        }

        sort = [("timestamp", -1)]

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/retrive",
            data={"query": query, "sort": sort}
        )

        if result["result"] is None:
            return None

        return result["result"]["data"]["humidity"]
