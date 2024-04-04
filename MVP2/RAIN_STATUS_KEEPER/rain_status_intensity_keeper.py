import requests


class RainStatusKeeper():

    def __init__(self, getway):
        self.getway = getway

    def register_rain_status(self, source_name, service_name, rain_status, timestamp):

        data = {
            "source_name": source_name,
            "service_name": service_name,
            "timestamp": timestamp,
            "type": "rain_status",
            "data": {
                "rain_status": rain_status
            }
        }

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/register",
            data={"data": data}
        )

        return result

    def retrive_last_rain_status(self):

        query = {
            "type": "rain_status"
        }

        sort = [("timestamp", -1)]

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/retrive",
            data={"query": query, "sort": sort}
        )

        if result["result"] is None:
            return None

        return result["result"]["data"]["rain_status"]
