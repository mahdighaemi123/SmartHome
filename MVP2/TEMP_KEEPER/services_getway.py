import requests


class ServicesGetway():

    def __init__(self, connection_string, service_call_endpoint="/services/call") -> None:
        self.connection_string = connection_string
        self.service_call_endpoint = service_call_endpoint

    def service_call(self, service_name, endpoint, data):
        return requests.post(self.connection_string+self.service_call_endpoint,
                             json={
                                 "service_name": service_name,
                                 "endpoint": endpoint,
                                 "data": data,
                             }).json()
