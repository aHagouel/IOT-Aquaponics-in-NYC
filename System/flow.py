#!/usr/bin/python
import requests
import time
from datetime import datetime
import schedule
import RPi.GPIO as GPIO

# Goal is to turn a pump on for 15 minutes every ~3.5 hours.

global turned_on
turned_on = False


def turn_pump_off():
    global turned_on
    try:
        requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/KEY_SECRET',
                  params={"value1": "none", "value2": "none", "value3": "none"})
        turned_on = False
        print("Turned pump off at "+str(datetime.fromtimestamp(time.time())))

    except:
        #Keep trying to turn pump off! #NoFloodsPlz
        print(">>>>> Exception found, trying to turn pump off at "+str(datetime.fromtimestamp(time.time())))
        turn_pump_off()
        

def turn_pump_on():
    global turned_on
    try:
        requests.post('https://maker.ifttt.com/trigger/turn_pump_on/with/key/KEY_SECRET',
                  params={"value1": "none", "value2": "none", "value3": "none"})
        turned_on = True
        print("Turned pump on at "+ str(datetime.fromtimestamp(time.time())))
        
    except:
        print(">>>>> Exception found, trying to turn pump off at "+str(datetime.fromtimestamp(time.time())))
        turn_pump_off()
        
        
def run_pump_sequence():
        # Make sure everything is off.
    # IFTTT takes some time to respond, so adding a buffer after every call.
    global turned_on
    if turned_on:
        turn_pump_off()
        time.sleep(5)
        turned_on = False

    # If outside my sleepy hours, turn pump on for 15 min duration.
    print("Starting flood sequence at " + str(datetime.now()))
    stop = time.time() + 60*20
    while (time.time() < stop):
        # Don't know how to read plug status just yet, so will assume
        # it all works until I actually code up some error handling :)
        if not turned_on:
            turn_pump_on()
            time.sleep(5)
            turned_on = True
            continue
        time.sleep(5)
    
    # Flood duration done, so turn off pump if it's on.
    if turned_on:
        print("Initiating drain sequence at " + str(datetime.fromtimestamp(time.time())))
        turn_pump_off()
        time.sleep(5)
        turned_on = False


schedule.every().day.at("08:30").do(run_pump_sequence)
schedule.every().day.at("11:00").do(run_pump_sequence)
schedule.every().day.at("14:00").do(run_pump_sequence)
schedule.every().day.at("17:00").do(run_pump_sequence)
schedule.every().day.at("20:00").do(run_pump_sequence)

while True:
    schedule.run_pending()
    time.sleep(5)

