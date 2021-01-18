#!/usr/bin/python
from time import sleep
from lobe import ImageModel
import subprocess 

#Learning mostly from https://blog.paperspace.com/tensorflow-lite-raspberry-pi/
# and https://github.com/microsoft/TrashClassifier. Took some code from my old project:
# https://github.com/aHagouel/MauiBot4000/blob/master/src/bot.py

model_folder = "/home/pi/Development/IOT-Aquaponics-in-NYC/Utilities/Image_classifier/"

# Load Lobe.ai TF model. Requires TF Lite & Lobe installation.
model = ImageModel.load(model_folder)

def take_picture(file_path = '/home/pi/Development/IOT-Aquaponics-in-NYC/Utilities/current_state'):
    command = "fswebcam -S 12 -r 980x540 --no-banner " + file_path + '.jpg'
    process = subprocess.call(command.split(), stdout=subprocess.PIPE)
    return file_path + '.jpg'

while True:
    photo_path = take_picture()
    # Run photo through Lobe TF model
    result = model.predict_from_file(photo_path)
    print(result)
    sleep(30)