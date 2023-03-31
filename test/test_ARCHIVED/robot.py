##from gpiozero import Robot
##import time
##
##robot = Robot(left = (7, 8), right = (9, 10))
##while True:
##	robot.forward()
##	time.sleep(3)
##	robot.stop()
##	robot.right()
##	time.sleep(1)
##	robot.stop()

import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

##Forward=19
##Backward=16
L1=16
L2=19
R1=20
R2=26
enL=3
enR=2
sleeptime=1

GPIO.setmode(GPIO.BCM) 
##GPIO.setmode(GPIO.BOARD)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(enL, GPIO.OUT)
GPIO.setup(enR, GPIO.OUT)

##GPIO.output(enL, GPIO.HIGH)
##GPIO.output(enR, GPIO.HIGH)
L=GPIO.PWM(enL, 200)
R=GPIO.PWM(enR, 200)
L.start(30)
R.start(30)
##L.ChangeDutyCycle(20)
##R.ChangeDutyCycle(20)

def lmotor(x):
    GPIO.output(L1,GPIO.HIGH)
    print("Left Forward")
    time.sleep(x)
    GPIO.output(L1, GPIO.LOW)
    
    GPIO.output(L2, GPIO.HIGH)
    print("Left Backward")
    time.sleep(x)
    GPIO.output(L2, GPIO.LOW)

def rmotor(x):
    GPIO.output(R1,GPIO.HIGH)
    print("Right Forward")
    time.sleep(x)
    GPIO.output(R1, GPIO.LOW)
    
    GPIO.output(R2, GPIO.HIGH)
    print("Right Backward")
    time.sleep(x)
    GPIO.output(R2, GPIO.LOW)
    
def forward(x):
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(R1, GPIO.LOW)

def reverse(x):
    GPIO.output(L2, GPIO.HIGH)
    GPIO.output(R2, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def left(x):
    L.start(35)
    GPIO.output(L2, GPIO.HIGH)
    GPIO.output(R1, GPIO.HIGH)
    print("Turning Left")
    time.sleep(x)
    GPIO.output(L2, GPIO.LOW)
    GPIO.output(R1, GPIO.LOW)
    
def right(x):
    L.start(35)
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(R2, GPIO.HIGH)
    print("Turning Right")
    time.sleep(x)
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)
    
while (1):
##    lmotor(5)
##    rmotor(5)
    forward(3)
    time.sleep(1)
    reverse(3)
    time.sleep(1)
    left(2)
    time.sleep(1)
    right(2)
    GPIO.cleanup()
