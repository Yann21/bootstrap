#!/usr/bin/env python3
from yeelight import Bulb
import click
import sys

bulb = Bulb("192.168.178.90")
step = 20

def change_brightness(amount):
    current_bright = int(bulb.get_properties()["bright"])
    bulb.set_brightness(current_bright + amount)

@click.command()
@click.argument("command")
def main(command):
    if (command == "toggle"):
        bulb.toggle()
    elif (command == "up"):
        change_brightness(+step)
    elif (command == "down"):
        change_brightness(-step)
    else:
        print("command not recognized")

if __name__ == "__main__":
    main()
