#!/usr/bin/python

'''Take a picture every X minutes and save it to ~/timelapse as y-m-d-h-m.jpg'''

import os
import time
from picamera import PiCamera
from datetime import datetime

# Start camera, set resolution and framerate
# lock ISO,shutter speed, white balance

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.framerate = 15
camera.iso = 100
time.sleep(2)
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

#take a picture every 5 minutes
while True:
    camera.capture('/media/Usb-Drive/Timelapse/{:%Y-%m-%d-%H-%M}.jpg'.format(datetime.now()))
    time.sleep(60)


#camera.start_preview()
#time.sleep(5)
#camera.capture('/home/pi/Desktop/{:%Y-%m-%d-%H-%M}.jpg'.format(datetime.now()))on
#camera.stop_preview()
