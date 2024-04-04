from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton

from Services.Display.service import DisplayerService


class LoggerService(Service, Singleton):
    def init(self,name,source_name, save_max_log=10, display_max_log=4):
        self.name = name
        self.source_name = source_name

        self.displayerService = DisplayerService()
        self.logs = []
        self.save_max_log = save_max_log
        self.display_max_log = display_max_log

    def clear_old_logs(self):
        len_logs = len(self.logs)
        if len_logs > self.save_max_log:
            self.logs = self.logs[len_logs-self.save_max_log:]

    def save_log(self, log):
        self.logs.append(log)
        self.clear_old_logs()

    def print_log(self, log):
        print(log)

    def display_logs(self):
        len_logs = len(self.logs)

        if len_logs > self.save_max_log:
            logs = self.logs[len(self.logs)-self.display_max_log:]
        else:
            logs = self.logs

        self.displayerService.display_lines(logs)

    def log(self, log):
        self.save_log(log)
        self.print_log(log)
        self.display_logs()

    def loop(self):
        pass
