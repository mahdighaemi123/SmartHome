from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Network.service import NetworkService

class GetwayService(Service, Singleton):
    def init(self, name, source_name, getway_url, getway_service_call_endpoint):
        self.name = name
        self.source_name = source_name
        self.getway_url = getway_url
        self.getway_service_call_endpoint = getway_service_call_endpoint

        self.networkService = NetworkService()

    def service_call(self, service_name, endpoint, data):
        return self.networkService.post_request(url=self.getway_url+self.getway_service_call_endpoint,
                                                data={
                                                    "service_name": service_name,
                                                    "endpoint": endpoint,
                                                    "data": data,
                                                })

    def loop(self):
        pass