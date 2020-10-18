import requests
import time

# Goal is to turn a pump on for 30 seconds every 30 minutes.

while True:
    # Make sure everything is off
    off = requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/SECRETS_HERE',
                        params={"value1":"none","value2":"none","value3":"none"})
    time.sleep(5)

    turned_on = False
    stop = time.time() + 30

    while time.time() < stop:

        # Don't know how to read plug status just yet, so will assume
        # it all works until I actually code up some error handling :)
        if not turned_on:
            on = requests.post('https://maker.ifttt.com/trigger/turn_pump_on/with/key/SECRETS_HERE',
                                params={"value1": "none", "value2": "none", "value3": "none"})
            turned_on = True
            time.sleep(5)
            continue

        # TODO: Flow rate monitoring w/ Raspberry Pi

        time.sleep(5)

    off = requests.post('https://maker.ifttt.com/trigger/turn_pump_off/with/key/SECRETS_HERE',
                        params={"value1":"none","value2":"none","value3":"none"})
    time.sleep(60*30)