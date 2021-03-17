#!/usr/bin/env python3
from yeelight import Bulb
import sys

bulb = Bulb("192.168.178.90")

def change_brightness(amount):
    current_bright = int(bulb.get_properties()["bright"])
    bulb.set_brightness(current_bright + amount)

arg = sys.argv[1]
step = 20

# Control flow
if (arg == "toggle"):
    bulb.toggle()
elif (arg == "up"):
    change_brightness(+step)
elif (arg == "down"):
    change_brightness(-step)
else:
    print("command not recognized")
