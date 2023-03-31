import RPi.GPIO as GPIO
import time

##GPIO.setmode(GPIO.BOARD)
##
##GPIO.setup(7, GPIO.OUT)
##pwm = GPIO.PWM(7, 50)
##pwm.start(0)
##
##def SetAngle(angle):
##    duty = angle/180 + 2
##    GPIO.output(7, 1)
##    pwm.ChangeDutyCycle(duty)
##    time.sleep(0.3)
##    GPIO.output(7, 0)
##    pwm.ChangeDutyCycle(0)
##
##SetAngle(1)
##
##pwm.stop()
##GPIO.cleanup()


servo_1 = 24   # Bottom mortor for turning left/right
servo_2 = 17   # 2nd bottom mortor
servo_3 = 27   # 3rd bottom mortor
servo_4 = 22   # 4th bottom mortor
servo_5 = 23   # 5th bottom mortor for rotating hand
servo_6 = 4     # Top mortor for hand

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1, GPIO.OUT)
GPIO.setup(servo_2, GPIO.OUT)
GPIO.setup(servo_3, GPIO.OUT)
GPIO.setup(servo_4, GPIO.OUT)
GPIO.setup(servo_5, GPIO.OUT)
GPIO.setup(servo_6, GPIO.OUT)

p_1 = GPIO.PWM(servo_1, 50) # GPIO 18 for PWM with 50Hz
p_1.start(0.1) # Initialization
p_2 = GPIO.PWM(servo_2, 50) # GPIO 17 for PWM with 50Hz
p_2.start(0.1) # Initialization
p_3 = GPIO.PWM(servo_3, 50) # GPIO 27 for PWM with 50Hz
p_3.start(0.1) # Initialization
p_4 = GPIO.PWM(servo_4, 50) # GPIO 22 for PWM with 50Hz
p_4.start(0.1) # Initialization
p_5 = GPIO.PWM(servo_5, 50) # GPIO 23 for PWM with 50Hz
p_5.start(0.1) # Initialization
p_6 = GPIO.PWM(servo_6, 50) # GPIO 4 for PWM with 50Hz
p_6.start(0.1) # Initialization

dc_1 = 7   # servo_1 home position
dc_2 = 9  # servo_2 home position
dc_3 = 2  # servo_3 home position
dc_4 = 4  # servo_4 home position
dc_5 = 1.5  # servo_5 home position
dc_6 = 6  # servo_6 home position

dc_conv = 7.5 / 90

def turn_left(angle):
  step = angle * dc_conv / 1000
  dc = dc_1
  count = 0 
  while count <1000:
    p_1.ChangeDutyCycle(dc)
    time.sleep(0.001)
    count = count + 1
    dc = dc + step
  return dc

def turn_right(angle):
  step = angle * dc_conv / 1000
  dc = dc_1
  count = 0 
  while count <1000:
    p_1.ChangeDutyCycle(dc)
    time.sleep(0.001)
    count = count + 1
    dc = dc - step
  return dc

def turn_home(current_dc):
  dc = current_dc
  count = 0
  if dc != dc_ini:
    step = (dc - dc_ini) / 1000
    while count < 1000:
      p_1.ChangeDutyCycle(dc)
      time.sleep(0.001)
      count = count + 1
      dc = dc - step
  else:
    p_1.stop()

def hand_open():
  p_6.ChangeDutyCycle(3)
  p_6.stop()

def hand_close():
  step = 2 / 1000
  dc = dc_6
  count = 0 
  while count <1000:
    p_6.ChangeDutyCycle(dc)
    time.sleep(0.001)
    count = count + 1
    dc = dc + step
    
##try:
##  r = 0
##  while r < 2:
####    p.ChangeDutyCycle(3)
####    time.sleep(1)
####    p.ChangeDutyCycle(3)
####    time.sleep(1)
####    p.ChangeDutyCycle(3)
####    time.sleep(1)
##    p.ChangeDutyCycle(4)
##    time.sleep(1)
##    p.ChangeDutyCycle(5)
##    time.sleep(1)
##    p.ChangeDutyCycle(6)
##    time.sleep(1)
##    p.ChangeDutyCycle(7)
##    time.sleep(1)
##    p.ChangeDutyCycle(8)
##    time.sleep(1)
####    p.ChangeDutyCycle(9)
####    time.sleep(1)
##    r += 1
##except KeyboardInterrupt:
##  p.stop()
##  GPIO.cleanup()
##
##p.ChangeDutyCycle(0)

dc_ini =7
s = 0
ss = 0
dc = dc_ini

while s <1000:
  p.ChangeDutyCycle(dc)
  time.sleep(0.001)
  s = s + 1
  dc = dc_ini + s*0.002
  
time.sleep(1)
print(dc)

dc_ini = dc
while ss < 1000:
  p.ChangeDutyCycle(dc)
  time.sleep(0.001)
  ss += 1
  dc = dc_ini - ss*0.002

time.sleep(1)
print(dc)

p.stop()

