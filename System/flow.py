import requests
import time
from datetime import datetime
import RPi.GPIO as GPIO

# Goal is to turn a pump on for 15 minutes every 4 hours.

global pulses, turned_on
pulses = 0
turned_on = False

FLOW_SENSOR = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def turn_pump_off():
    global turned_on
    try:
        requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/SECRETS_HERE',
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
        requests.post('https://maker.ifttt.com/trigger/turn_pump_on/with/key/SECRETS_HERE',
                  params={"value1": "none", "value2": "none", "value3": "none"})
        turned_on = True
        print("Turned pump on at "+ str(datetime.fromtimestamp(time.time())))
        
    except:
        turn_pump_off()
        print(">>>>> Exception found, trying to turn pump off at "+str(datetime.fromtimestamp(time.time())))
        

# Callback when gpio pin changes value, signifying flow meter pulse. Keep simple right now to a count, but
# in the future can actually count up the amount of water that's passed through the system.
def pulseCallback(channel):
    global pulses
    pulses += 1
    print("Detected water draining at " + str(datetime.fromtimestamp(time.time()))+ ", pulses up to " + str(pulses))


GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=pulseCallback)

print("Starting control program at " + str(datetime.fromtimestamp(time.time())))
while True:
    # Make sure everything is off.
    # IFTTT takes some time to respond, so adding a buffer after every call.
    if turned_on:
        turn_pump_off()
        time.sleep(5)
        turned_on = False  

    stop = time.time() + 60*15

    # Turn pump on for flood duration.
    # TODO: Don't run during night time
    while time.time() < stop:
        
        # Don't know how to read plug status just yet, so will assume
        # it all works until I actually code up some error handling :)
        if not turned_on:
            turn_pump_on()
            time.sleep(5)
            turned_on = True
            continue

        time.sleep(5)

    # Either time ran out or drain began, so turn off pump if it's not already
    if turned_on:
        print("Initiating drain sequence at " + str(datetime.fromtimestamp(time.time())))
        turn_pump_off()
        time.sleep(5)
        turned_on = False

    print("ZzzzZZZzzzzzzZZZZZ ...Sleeping for 4 hours ... ZzzzZZZzzzzzzZZZZZ")
    time.sleep(60*60*4)
