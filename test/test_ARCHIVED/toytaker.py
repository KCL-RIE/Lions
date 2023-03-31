import picamera
import time

# camera = picamera.PiCamera()
# use try/finally (camera.close) block approach    or... use contxt manger protocol:

# Set-up camera such that it closes when we're done
print("About to take pic... ")
with picamera.PiCamera() as camera:
	for n in range(6):
		filename = "/home/ubuntu/images/toys/t_image" + str(n+148) + ".jpg"
		camera.resolution = (1280, 840)
		camera.brightness = 59
		#camera.contrast = 50
		camera.capture(filename)
		print("Pic %s successfully taken!" % (n+1))
		time.sleep(0.1)
