# Goal is to turn a pump on for 30 seconds every 30 minutes.

import requests
import time
import RPi.gpio as GPIO

FLOW_SENSOR = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN)

def turn_pump_off():
    requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/SECRETS_HERE',
                  params={"value1": "none", "value2": "none", "value3": "none"})
    print("Turned pump off at "+str(time.time()))

def turn_pump_on():
    requests.post('https://maker.ifttt.com/trigger/turn_pump_on/with/key/SECRETS_HERE',
                  params={"value1": "none", "value2": "none", "value3": "none"})
    print("Turned pump on at "+str(time.time()))


while True:
    # Make sure everything is off
    turn_pump_off()

    #IFTTT takes a second to respond.
    time.sleep(5)

    turned_on = False
    stop = time.time() + 30
    while time.time() < stop:

        # Don't know how to read plug status just yet, so will assume
        # it all works until I actually code up some error handling :)
        if not turned_on:
            turn_pump_on()
            turned_on = True
            time.sleep(5)
            continue
        # TODO: Tests this works when you get a monitor for Pi
        # Check if overflow initiated from grow bed, turn pump off to drain
        if GPIO.input(FLOW_SENSOR) != 0:
            turn_pump_off()
            time.sleep(5)
            continue

        time.sleep(5)

    turn_pump_off()
    time.sleep(60*30)