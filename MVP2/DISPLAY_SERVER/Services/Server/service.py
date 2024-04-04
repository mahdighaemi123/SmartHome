from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Network.service import NetworkService
from .Interfaces.micropyserver import MicroPyServer
from .Interfaces.utils import *


class ServerService(Service, Singleton):
    def init(self, name, source_name, port=80, host="0.0.0.0"):
        self.name = name
        self.source_name = source_name
        self.port = port
        self.host = host

        self.server = MicroPyServer(host=host, port=port)
        self.networkService = NetworkService()

    def loop(self):
        if self.networkService.is_connected():
            self.server.non_blocking_loop_once()

    def add_route(self, route, handler, method="GET"):

        def middleware(request):
            method = get_request_method(request)
            path = get_request_path(request)
            query = get_request_query_params(request)
            body = get_request_post_params(request)

            if query != None:
                for key, value in query.items():
                    query[key] = unquote(value)

            request = {
                "method": method,
                "path": path,
                "query": query,
                "body": body,
            }

            return handler(request)

        self.server.add_route(route, middleware, method)

    def send_response(self, response, http_code=200, content_type="text/html", extend_headers=None):
        send_response(self.server, response, http_code=http_code,
                      content_type=content_type, extend_headers=extend_headers)

    def send_json_response(self, data, http_code=200, content_type="application/json", extend_headers=None):
        send_json_response(self.server, data, http_code=http_code,
                           content_type=content_type, extend_headers=extend_headers)
