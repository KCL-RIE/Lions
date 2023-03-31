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


servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 4 for PWM with 50Hz
p.start(1) # Initialization

dc_ini = 7.2
s = 0
ss = 0
dc = dc_ini
dc_6 = 6

##def turn_left(angle):
##  s = 0
##  dc_conv = 7.5 / 90
##  step = (angle * 7.5 / 90) / 1000
##  dc = dc_ini
##  while s <1000:
##    p.ChangeDutyCycle(dc)
##    time.sleep(0.001)
##    s = s + 1
##    dc = dc + step
##    
##  print('current_dc: ', dc)
##  return dc
##
##def turn_right(angle):
##  s = 0
##  dc_conv = 7.5 / 90
##  step = (angle * 7.5) / (1000 * 90)
##  dc = dc_ini
##  while s <1000:
##    p.ChangeDutyCycle(dc)
##    time.sleep(0.001)
##    s = s + 1
##    dc = dc - step
##    
##  print('current_dc: ', dc)
##  return dc
##
##def turn_home(current_dc):
##  dc = current_dc
##  count = 0
##  if dc != dc_ini:
##    step = (dc - dc_ini) /1000
##    while count < 1000:
##      p.ChangeDutyCycle(dc)
##      time.sleep(0.001)
##      count = count + 1
##      dc = dc - step
##  else:
##    p.stop()

def hand_open():
  p.ChangeDutyCycle(3)
  time.sleep(1)
  p.stop()

def hand_close():
  step = 2 / 1000
  dc = dc_6
  print(dc)
  count = 0 
  while count <1000:
    p.ChangeDutyCycle(dc)
    time.sleep(0.001)
    count = count + 1
    dc = dc + step
  print(dc)
  
##while s <1000:
##  p.ChangeDutyCycle(dc)
##  time.sleep(0.001)
##  s = s + 1
##  dc = dc_ini + s*0.002
##  
##time.sleep(1)
##print(dc)
##
##dc_ini = dc
##while ss < 1000:
##  p.ChangeDutyCycle(dc)
##  time.sleep(0.001)
##  ss += 1
##  dc = dc_ini - ss*0.002
##
##time.sleep(1)
##print(dc)


##dc = turn_left(30)
##print(dc)
##time.sleep(1)
##turn_home(dc)
##time.sleep(1)
##dc = turn_right(30)
##print(dc)
##time.sleep(1)
##turn_home(dc)
##time.sleep(1)

hand_open()
time.sleep(1)
hand_close()
time.sleep(1)
hand_open()
time.sleep(1)

p.stop()

