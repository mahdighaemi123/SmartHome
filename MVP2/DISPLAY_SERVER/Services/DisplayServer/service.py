from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Server.service import ServerService
from Services.Display.service import DisplayService
from Services.Logger.service import LoggerService

import json


class DisplayServerService(Service, Singleton):
    def init(self, name, source_name):
        self.name = name
        self.source_name = source_name
        self.serverService = ServerService()
        self.displayService = DisplayService()
        self.loggerService = LoggerService()

        self.serverService.add_route("/", self.index_handler, "GET")
        self.serverService.add_route("/display", self.display_handler, "GET")

    def index_handler(self, request):
        self.loggerService.log("request -> indeex page")
        self.serverService.send_json_response(
            {"status": True, "message": "display server is running"})

    def display_handler(self, request):
        self.loggerService.log("request -> display service")
        self.loggerService.log(f"{request}")

        query = request["query"]
        lines = query["lines"]

        if isinstance(lines, str):
            lines = json.loads(lines)

        self.displayService.display_lines(lines)

        self.serverService.send_json_response(
            {"status": True, "message": "display successful"})

    def loop(self):
        pass
