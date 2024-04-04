from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton


class LoggerService(Service, Singleton):
    def init(self, name, source_name, save_max_log=10):
        self.name = name
        self.source_name = source_name

        self.logs = []
        self.save_max_log = save_max_log

    def clear_old_logs(self):
        len_logs = len(self.logs)
        if len_logs > self.save_max_log:
            self.logs = self.logs[len_logs-self.save_max_log:]

    def save_log(self, log):
        self.logs.append(log)
        self.clear_old_logs()

    def print_log(self, log):
        print(log)

    def log(self, log):
        self.save_log(log)
        self.print_log(log)

    def loop(self):
        pass
