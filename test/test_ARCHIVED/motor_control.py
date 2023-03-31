import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Allowed_Distance = 50

L1A = 20         # GPIO20
L2A = 26       # GPIO26
R3A = 17        # GPIO17
R4A = 27        # GPIO27
enL = 14         # GPIO5
enR = 15         # GPIO6

GPIO.setup(L1A, GPIO.OUT)       # initialize GPIO2 as an output
GPIO.setup(L2A, GPIO.OUT)
GPIO.setup(R3A, GPIO.OUT)
GPIO.setup(R4A, GPIO.OUT)
GPIO.setup(enL, GPIO.OUT)       # initialize GPIO5 as an output.
GPIO.setup(enR, GPIO.OUT)       # initialize GPIO6 as an output.

pA = GPIO.PWM(enL, 100)        #GPIO5 as PWM output, with 100Hz frequency
pB = GPIO.PWM(enR, 100)

#pA.start(0)                            #generate PWM signal with 0% duty cycle
#pB.start(0)

pA.ChangeDutyCycle(40)                 #change duty cycle
pB.ChangeDutyCycle(40)

# Set forward movement
def FORWARD():
  GPIO.output(L1A, 0)
  GPIO.output(L2A, 1)
  GPIO.output(R3A, 0)
  GPIO.output(R4A, 1)
  return

# Set reverse movement
def REVERSE():
  GPIO.output(L1A, 1)
  GPIO.output(L2A, 0)
  GPIO.output(R3A, 1)
  GPIO.output(R4A, 0)
  return

# Turn left
def LEFT():
  GPIO.output(L1A, 1)
  GPIO.output(L2A, 0)
  GPIO.output(R3A, 0)
  GPIO.output(R4A, 1)
  return

# Turn right
def RIGHT():
  GPIO.output(L1A, 0)
  GPIO.output(L2A, 1)
  GPIO.output(R3A, 1)
  GPIO.output(R4A, 0)
  return

# Stop
def STOP():
  GPIO.output(L1A, 0)
  GPIO.output(L2A, 0)
  GPIO.output(R3A, 0)
  GPIO.output(R4A, 0)
  return


while True:
    LEFT()
    time.sleep(2)
    RIGHT()
    time.sleep(2)
    FORWARD()
    time.sleep(3)
    REVERSE()
    time.sleep(3)
    
    if 0xFF == ord('q'):
        break 

STOP()
    
