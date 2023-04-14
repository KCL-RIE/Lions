# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep


'''
--------------BACK----------------
----------------------------------
LR              |   RR
  LRENA         |     RRENA
  LRIN1, LRIN2  |     RRIN1, RRIN2
                |     
                |
                |
LF              |   RF
  LFENB         |     RFENB
  LFIN3, LFIN4  |     RFIN3, FRIN4
----------------|-----------------
-------------PROPENA--------------
---------------PROPIN1------------
---------------PROPIN2------------
----------------|-----------------
----------------------------------
-------------FRONT----------------
'''


LRENA = 2
LRIN1 = 3
LRIN2 = 4

LFENB = 17
LFIN3 = 27
LFIN4 = 22

RRENA = 25
RRIN1 = 8
RRIN2 = 7

RFENB = 21
RFIN3 = 16
RFIN4 = 20

PROPENA = 18
PROPIN1 = 23
PROPIN2 = 24

#############

# LRIN1 = 24
# LRIN2 = 23
# en = 25
temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(PROPIN1,GPIO.OUT)
GPIO.setup(PROPIN2,GPIO.OUT)
GPIO.setup(PROPENA,GPIO.OUT)

GPIO.output(PROPIN1,GPIO.LOW)
GPIO.output(PROPIN2,GPIO.LOW)
p=GPIO.PWM(PROPENA,1000)


##################


p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(PROPIN1,GPIO.HIGH)
         GPIO.output(PROPIN2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(PROPIN1,GPIO.LOW)
         GPIO.output(PROPIN2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(PROPIN1,GPIO.LOW)
        GPIO.output(PROPIN2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(PROPIN1,GPIO.HIGH)
        GPIO.output(PROPIN2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(PROPIN1,GPIO.LOW)
        GPIO.output(PROPIN2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(12)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(15)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
