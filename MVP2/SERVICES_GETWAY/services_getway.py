import requests
import utils


class ServicesGetway():

    def __init__(self, services):
        self.services = services
        self.handlers = {
            "GET": self.get_handler,
            "POST": self.post_handler
        }

    def get_handler(self, url, data):
        url_with_data = utils.add_params_to_url(url, data)
        return requests.get(url_with_data).json()

    def post_handler(self, url, data):
        return requests.post(url, json=data).json()

    def default_handler(self, url, data):
        raise ValueError("not implimented reqested method")

    def call(self, service_name, endpoint, data):
        url = self.services[service_name]["address"] + endpoint
        method = self.services[service_name]["method"].upper()
        return self.handlers[method](url, data)
