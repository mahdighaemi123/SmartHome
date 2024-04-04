from BaseInterfaces.sevice import Service
from BaseInterfaces.singleton import Singleton
from .Interfaces.displayer_driver import DisplayerDriver


class DisplayerService(Service, Singleton):
    def init(self,name,source_name, scl_pin, sda_pin, width, height, line_height=8):
        self.name = name
        self.source_name = source_name
        
        self.displayerDriver = DisplayerDriver(
            scl_pin=scl_pin,
            sda_pin=sda_pin,
            width=width,
            height=height,
            line_height=line_height
        )

    def display_lines(self, lines):
        self.clear()
        
        for index, line in enumerate(lines):
            self.display_line(line, index)

        self.show()

    def clear(self):
        self.displayerDriver.clear()

    def display_line(self, text, line):
        self.displayerDriver.display_line(text, line)

    def show(self):
        self.displayerDriver.show()

    def loop(self):
        pass
