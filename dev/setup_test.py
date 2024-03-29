import pycom
import time

RED = 0xFF0000
YELLOW = 0xFFFF33
GREEN = 0x007F00
OFF = 0x000000

def set_led_to(color=GREEN):
    pycom.heartbeat(False) # Disable the heartbeat LED
    pycom.rgbled(color)

def flash_led_to(color=GREEN, t1=2):
    set_led_to(color)
    time.sleep(t1)
    set_led_to(OFF)

flash_led_to(RED)
flash_led_to(YELLOW)
set_led_to(OFF)
