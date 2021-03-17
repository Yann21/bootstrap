#!/usr/bin/env python3
from yeelight import Bulb
import sys

bulb = Bulb("192.168.178.90")

def change_brightness(amount):
    current_bright = int(bulb.get_properties()["bright"])
    bulb.set_brightness(current_bright + amount)

try:
    arg = sys.argv[1]
except IndexError as e:
    raise("wrong usage")

if (arg =="red"):
    bulb.set_rgb(180, 80, 80)
elif (arg == "dimmed"):
    bulb.set_rgb(230, 180, 180)
elif (arg == "white"):
    bulb.set_rgb(230, 230, 220)
else:
    print("command not recognized")
