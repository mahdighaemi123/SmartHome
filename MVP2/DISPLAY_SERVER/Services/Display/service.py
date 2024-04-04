from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton
from .Interfaces.displayer_driver import DisplayerDriver


class DisplayService(Service, Singleton):
    def init(self, name, source_name, scl_pin, sda_pin, num_cols, num_rows, i2c_addr=0x27, freq=800000):
        self.name = name
        self.source_name = source_name

        self.displayerDriver = DisplayerDriver(
            scl_pin=scl_pin,
            sda_pin=sda_pin,
            num_cols=num_cols,
            num_rows=num_rows,
            i2c_addr=i2c_addr,
            freq=freq
        )

    def display_lines(self, lines):
        for index, line in enumerate(lines):
            self.display_line(line, index)

    def clear(self):
        self.displayerDriver.clear()

    def display_line(self, text, line):
        self.displayerDriver.display_line(text, line)

    def loop(self):
        pass
