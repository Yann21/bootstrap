#!/usr/bin/env python3
from yeelight import *
from yeelight import Bulb
from time import sleep
from datetime import datetime, date, time, timedelta

bulb = Bulb("192.168.178.90")
bulb.turn_off()
bulb.set_brightness(0)
bulb.set_color_temp(1000)

# bulb.set_rgb(255, 255, 0)
# bulb.set_hsv(100, 320, 0)


def fade(start, end):
    current_time = datetime.now().time()

    now = datetime.now()
    deltoid = timedelta(hours=now.hour, minutes=now.minute, seconds=now.second)

    progress = end - deltoid
    range = end - start
    brightness = (1 - progress/range) * 100

    print(brightness)
    bulb.set_brightness(brightness)

def do_until(action, until):
    end_time = datetime.combine(date.today(), time(0)) + until
    while datetime.now() < end_time:
        action()
        sleep(2)

def fade_in(start, end):
    do_until(lambda: None, start)
    bulb.turn_on()
    do_until(lambda: fade(start, end), end)

start = timedelta(hours=22, minutes=30, seconds=0)
end = timedelta(hours=22, minutes=59, seconds=0)
fade_in(start, end)

# if __name__ == "__main__":
#     while 1:
#         fade_in(datetime.time(7, 0, 0),
#                 datetime.time(7, 30, 0))
