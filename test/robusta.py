import time
import RPi.GPIO as GPIO

# Set GPIO Mode and Pin Numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MACL = 35
MBCL = 37
MA2CL = 40
MB2CL = 36

# Setup GPIO pins for motor control
GPIO.setup(MACL, GPIO.OUT)
GPIO.setup(MBCL, GPIO.OUT)
GPIO.setup(MA2CL, GPIO.OUT)
GPIO.setup(MB2CL, GPIO.OUT)

pwm1 = GPIO.PWM(MACL, 100)
pwm2 = GPIO.PWM(MBCL, 100)
pwm3 = GPIO.PWM(MA2CL, 100)
pwm4 = GPIO.PWM(MB2CL, 100)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

def move_forward(speed):
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)

def move_stop():
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(0)
    pwm4.ChangeDutyCycle(0)

while True:
    try:
        duty_cycle = 50
        move_forward(duty_cycle)
        time.sleep(10)
        move_stop()
        time.sleep(10)
    except KeyboardInterrupt:
        break

move_stop()
GPIO.cleanup()
