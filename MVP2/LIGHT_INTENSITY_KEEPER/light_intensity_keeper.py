import requests


class LightIntensityKeeper():

    def __init__(self, getway):
        self.getway = getway

    def register_light_intensity(self, source_name, service_name, light_intensity, timestamp):

        data = {
            "source_name": source_name,
            "service_name": service_name,
            "timestamp": timestamp,
            "type": "light_intensity",
            "data": {
                "light_intensity": light_intensity
            }
        }

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/register",
            data={"data": data}
        )

        return result

    def retrive_last_light_intensity(self):

        query = {
            "type": "light_intensity"
        }

        sort = [("timestamp", -1)]

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/retrive",
            data={"query": query, "sort": sort}
        )

        if result["result"] is None:
            return None

        return result["result"]["data"]["light_intensity"]
