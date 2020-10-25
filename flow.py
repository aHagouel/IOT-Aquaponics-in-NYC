import requests
import time
import RPi.GPIO as GPIO

# Goal is to turn a pump on for 3 minutes or until ebb & flow aquaponic system floods, every 30 minutes

global pulses
pulses = 0

FLOW_SENSOR = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def turn_pump_off():
    requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/SECRETS_HERE',
                  params={"value1": "none", "value2": "none", "value3": "none"})
    print("Turned pump off at "+str(time.time()))


def turn_pump_on():
    requests.post('https://maker.ifttt.com/trigger/turn_pump_on/with/key/SECRETS_HERE',
                  params={"value1": "none", "value2": "none", "value3": "none"})
    print("Turned pump on at "+str(time.time()))


# Callback when gpio pin changes value, signifying flow meter pulse. Keep simple right now to a count, but
# in the future can actually count up the amount of water that's passed through the system.
def pulseCallback(channel):
    global pulses
    pulses += 1
    print("Detected flowing water at " + str(time.time()))


GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=pulseCallback)

print("Starting control program at " + str(time.time()))
turned_on = False
while True:
    # Make sure everything is off.
    # IFTTT takes some time to respond, so adding a buffer after every call.
    if turned_on:
        turn_pump_off()
        time.sleep(5)
        turned_on = False

    global pulses
    localPulses = pulses
    stop = time.time() + 60*3

    # Turn pump on for duration OR until grow bed starts draining
    while time.time() < stop or localPulses < pulses:

        # Don't know how to read plug status just yet, so will assume
        # it all works until I actually code up some error handling :)
        if not turned_on:
            turn_pump_on()
            time.sleep(5)
            turned_on = True
            continue

        time.sleep(5)

    # Either time ran out or drain began, so turn off pump if it's not already
    print("Initiating drain sequence at " + str(time.time()))
    if turned_on:
        turn_pump_off()
        time.sleep(5)
        turned_on = False

    time.sleep(60*30)
