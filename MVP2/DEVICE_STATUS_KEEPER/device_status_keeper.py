import requests


class ServiceStateKeeper():

    def __init__(self, getway):
        self.getway = getway

    def register_device_status(self, source_name, service_name, device_status, timestamp):

        data = {
            "source_name": source_name,
            "service_name": service_name,
            "timestamp": timestamp,
            "type": "device_status",
            "data": {
                "device_status": device_status
            }
        }

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/register",
            data={"data": data}
        )

        return result

    def retrive_last_device_status(self):

        query = {
            "type": "device_status"
        }

        sort = [("timestamp", -1)]

        result = self.getway.service_call(
            service_name="DataKeeper",
            endpoint="/data/retrive",
            data={"query": query, "sort": sort}
        )

        if result["result"] is None:
            return None

        return result["result"]["data"]["device_status"]
