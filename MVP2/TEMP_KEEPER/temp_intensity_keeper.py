import requests


class TempKeeper():

    def __init__(self, getway):
        self.getway = getway

    def register_temp(self, source_name, service_name, temp, timestamp):

        data = {
            "source_name": source_name,
            "service_name": service_name,
            "timestamp": timestamp,
            "type": "temp",
            "data": {
                "temp": temp
            }
        }

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/register",
            data={"data": data}
        )

        return result

    def retrive_last_temp(self):

        query = {
            "type": "temp"
        }

        sort = [("timestamp", -1)]

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/retrive",
            data={"query": query, "sort": sort}
        )

        if result["result"] is None:
            return None

        return result["result"]["data"]["temp"]
