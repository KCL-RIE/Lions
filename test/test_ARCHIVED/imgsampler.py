import picamera
import time

# camera = picamera.PiCamera()
# use try/finally (camera.close) block approach    or... use contxt manger protocol:

# Set-up camera such that it closes when we're done
print("About to take pic... ")
with picamera.PiCamera() as camera:
	for n in range(5):
		filename = "/home/ubuntu/images/testimg" + str(n+1) + ".jpg"
		camera.resolution = (1280, 720)
		#camera.brightness = 100
		#camera.contrast = 50
		camera.capture(filename)
		print("Pic %s successfully taken!" % (n+1))
		time.sleep(4)
