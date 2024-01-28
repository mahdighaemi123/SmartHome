
import time
from machine import Pin, SoftI2C
import libs.ssd1306 as ssd1306

class Displayer():
    def __init__(self,scl_pin,sda_pin,width,height,line_height):
        i2c = SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin))
        oled = ssd1306.SSD1306_I2C(width, height, i2c)

        self.scl_pin=scl_pin
        self.sda_pin=sda_pin
        self.width=width
        self.height=height
        self.line_height=line_height
        self.oled=oled

    def display_line(self,text,line=0):
        self.oled.text(text, 0, line*self.line_height)

    def clear(self):
        self.oled.fill(0)

    def show(self):
        self.oled.show()

