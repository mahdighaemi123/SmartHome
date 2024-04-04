from machine import Pin, SoftI2C
from .lcd_i2c import LCD

class DisplayerDriver():
    def __init__(self,scl_pin,sda_pin,num_cols,num_rows,i2c_addr=0x27,freq=800000):
        self.i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=freq)
        self.lcd = LCD(addr=i2c_addr, cols=num_cols, rows=num_rows, i2c=self.i2c)

        self.scl_pin=scl_pin
        self.sda_pin=sda_pin
        self.num_cols=num_cols
        self.num_rows=num_rows
        self.i2c_addr=i2c_addr
        self.freq=freq

        self.lcd.begin()


    def display(self,text):
        self.lcd.print(text)

    def _add_extra_sapce_2_make_full_line(self,text):
        num_space = self.num_cols-len(text)
        extra_spaces = " " * num_space
        text += extra_spaces
        return text
    
    def display_line(self,text,line=0):
        self.lcd.set_cursor(col=0, row=line)
        self.display(self._add_extra_sapce_2_make_full_line(text))

    def clear(self):
        self.lcd.clear()