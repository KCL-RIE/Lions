import picamera
import time

# camera = picamera.PiCamera()
# use try/finally (camera.close) block approach    or... use contxt manger protocol:

# Set-up camera such that it closes when we're done
print("About to take pic... ")
with picamera.PiCamera() as camera:
	for n in range(4):
		filename = "/home/ubuntu/images/not_toys/nt_image" + str(n+99) + ".jpg"
		camera.resolution = (1280, 720)
		camera.brightness = 60
		#camera.contrast = 50
		camera.capture(filename)
		print("Pic %s successfully taken!" % (n+1))
		time.sleep(1)