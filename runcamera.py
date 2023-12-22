# import the necessary packages
from picamera import PiCamera
import time
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
# allow the camera to warmup
time.sleep(0.5)
# grab an image from the camera
camera.start_preview()
# Infinite Loop the camera
while True:
	time.sleep(1)



