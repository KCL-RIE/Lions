import RPi.GPIO as GPIO
import time

# Set GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)

class Motor:

	def __init__(self, INA1=35, INA2=33, INA3=31, INA4=23, INB1=38, INB2=36, INB3=32, INB4=26, ENAA=37, ENAB=21, ENBA=24, ENBB=40):
		# Set up GPIO pins for 1st motor controller
		GPIO.setup(INA1, GPIO.OUT)
		GPIO.setup(INA2, GPIO.OUT)
		GPIO.setup(INA3, GPIO.OUT)
		GPIO.setup(INA4, GPIO.OUT)

		# Set up GPIO pins for 2nd motor controller
		GPIO.setup(INB1, GPIO.OUT)
		GPIO.setup(INB2, GPIO.OUT)
		GPIO.setup(INB3, GPIO.OUT)
		GPIO.setup(INB4, GPIO.OUT)


		GPIO.setup(ENAA, GPIO.OUT)
		GPIO.setup(ENAB, GPIO.OUT)
		GPIO.setup(ENBA, GPIO.OUT)
		GPIO.setup(ENBB, GPIO.OUT)

		GPIO.setup(ENAA, GPIO.HIGH)
		GPIO.setup(ENAB, GPIO.HIGH)
		GPIO.setup(ENBA, GPIO.HIGH)
		GPIO.setup(ENBB, GPIO.HIGH)


		# Set up PWM for 1st motor controller
		self.PWMAA = GPIO.PWM(ENAA, 1000)
		self.PWMAB = GPIO.PWM(ENAB, 1000)
		# Set up PWM for 2nd motor controller
		self.PWMBA = GPIO.PWM(ENBA, 1000)
		self.PWMBB = GPIO.PWM(ENBB, 1000)

		# Start 1st motor controller
		self.PWMAA.start(50)
		# self.PWMAB.start(50)
		# self.PWMBA.start(50)
		# self.PWMBB.start(50)

	# @param speed  :  int between -100 and 100, where -VE values are reverse
	# @param strafe :  int between -100 and 100, where -VE values are left
	# @param turn   :  int between -100 and 100, where -VE values are anti-clockwise	
	def drive(self, speed, strafe, turn):
		# Speed Limit Accepted Values
		if(speed < -100):
			speed = -100
		if(speed > 100):
			speed = 100

		LFWSpeed = speed + strafe + turn
		LBWSpeed = speed - strafe + turn
		RFWSpeed = speed - strafe - turn
		RBWSpeed = speed + strafe - turn

		if(speed > 0):
			self.PWMAA.ChangeDutyCycle(0)
		# 	self.PWMA2.ChangeDutyCycle(abs(speed))
		# 	self.PWMA3.ChangeDutyCycle(0)
		# 	self.PWMA4.ChangeDutyCycle(abs(speed))

		# 	self.PWMB1.ChangeDutyCycle(0)
		# 	self.PWMB2.ChangeDutyCycle(abs(speed))
		# 	self.PWMB3.ChangeDutyCycle(0)
		# 	self.PWMB4.ChangeDutyCycle(abs(speed))

		# else:
		# 	self.PWMA1.ChangeDutyCycle(abs(speed))
		# 	self.PWMA2.ChangeDutyCycle(0)
		# 	self.PWMA3.ChangeDutyCycle(abs(speed))
		# 	self.PWMA4.ChangeDutyCycle(0)

		# 	self.PWMB1.ChangeDutyCycle(abs(speed))
		# 	self.PWMB2.ChangeDutyCycle(0)
		# 	self.PWMB3.ChangeDutyCycle(abs(speed))
		# 	self.PWMB4.ChangeDutyCycle(0)


	def stop(self):
		self.PWMA1.ChangeDutyCycle(0)
		self.PWMA2.ChangeDutyCycle(0)
		self.PWMA3.ChangeDutyCycle(0)
		self.PWMA4.ChangeDutyCycle(0)

		self.PWMB1.ChangeDutyCycle(0)
		self.PWMB2.ChangeDutyCycle(0)
		self.PWMB3.ChangeDutyCycle(0)
		self.PWMB4.ChangeDutyCycle(0)

		# Clean up GPIO pins
		GPIO.cleanup()


if __name__=="__main__":
	ENAA = 23
	ENAB = 29
	ENBA = 24
	ENBB = 26

	# 1st motor controller
	LFW1 = 31
	LFW2 = 33
	LBW1 = 35
	LBW2 = 37

	# 2nd motor controller
	RFW1 = 32
	RFW2 = 36
	RBW1 = 38
	RBW2 = 40

	speed = 100
	strafe = 0
	turn = 0

	# Lions Robot Drive!
	try:
		lions = Motor(LFW1, LFW2, LBW1, LBW2, RFW1, RFW2, RBW1, RBW2, ENAA, ENAB, ENBA, ENBB)
		lions.drive(speed, strafe, turn)

		#time.sleep(70)
		#lions.stop()

	except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
	   print("Keyboard interrupt")

	except:
	   print("Some Error") 

	finally:
	   print("Clean Up") 
	   GPIO.cleanup() # cleanup all GPIO 
