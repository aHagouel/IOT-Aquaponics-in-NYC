#!/usr/bin/python
import schedule
import time
from datetime import datetime
import requests

global turned_on
turned_on = False


def turn_lights_on():
    global turned_on
    try:
        requests.post('https://maker.ifttt.com/trigger/turn_lights_on/with/key/KEY_SECRET',
                      params={"value1": "none", "value2": "none", "value3": "none"})
        print("Turned lights on at " + str(datetime.fromtimestamp(time.time())))
        time.sleep(5)
        turned_on = True
    except:
        # Keep trying to turn lights on; plants need food!
        print(">>>>> Exception found, trying to turn lights on at " + str(datetime.fromtimestamp(time.time())))
        turn_lights_on()


def turn_lights_off():
    global turned_on
    try:
        requests.post('https://maker.ifttt.com/trigger/turn_lights_off/with/key/KEY_SECRET',
                      params={"value1": "none", "value2": "none", "value3": "none"})
        print("Turned lights off at " + str(datetime.fromtimestamp(time.time())))
        time.sleep(5)
        turned_on = False
    except:
        # Keep trying to turn lights on; plants need food!
        print(">>>>> Exception found, trying to turn lights off at " + str(datetime.fromtimestamp(time.time())))
        turn_lights_off()


schedule.every().day.at("08:30").do(turn_lights_on)
schedule.every().day.at("21:00").do(turn_lights_off)

while True:
    schedule.run_pending()
    time.sleep(5)
