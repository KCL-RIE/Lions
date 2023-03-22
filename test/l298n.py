#!/usr/bin/python3
# File name   : l298n.py
# Description : Control Mecanum Motors
# Author      : Minseok
# Date        : 2023/03/21


import RPi.GPIO as GPIO
import time


class L298N:
    """A class to control one side of an L298N dual H bridge motor driver with speed control."""

    '''
    -------------FRONT--------------
    --------------------------------
    LFW            |   RFW
      INB1, INB2   |     INA3, INA4
      ENBA         |     ENAB
                   |
                   |
    LBW            |   RBW
      ENBB         |     ENAA
      INB3, INB4   |     INA1, INA2
    --------------------------------
    --------------BACK--------------
    '''

    def __init__(self, ENAA, INA1, INA2, ENAB, INA3, INA4, ENBA, INB1, INB2, ENBB, INB3, INB4):
        self.INA1 = INA1
        self.INA2 = INA2
        self.INA1 = INA3
        self.INA2 = INA4
        self.INB1 = INB1
        self.INB2 = INB2
        self.INB3 = INB3
        self.INB4 = INB4

        self.ENAA = ENAA
        self.ENAB = ENAB
        self.ENBA = ENBA
        self.ENBB = ENBB

        GPIO.setwarnings(False)

        all_pins = [self.ENAA, self.INA1, self.INA2, self.ENAB, self.INA3, self.INA4, self.ENBA, self.INB1, self.INB2, self.ENBB, self.INB3, self.INB4]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(all_pins, GPIO.OUT)

    def forward(self, speed=100):
        pwm = GPIO.PWM(self.ENAA, 800)
        pwm.start(speed)
        GPIO.output(self.INA1, 1)
        GPIO.output(self.INA2, 0)

    def backward(self, speed=100):
        pwm = GPIO.PWM(self.ena, 800)
        pwm.start(speed)
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 1)

    def stop(self):
        pwm = GPIO.PWM(self.ena, 800)
        pwm.stop()
        GPIO.output(self.ena, 0)
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 0)

    def cleanup(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)


    def drive(self, speed=100, strafe=0, turn=0):
        GPIO.setwarnings(False)

        # Speed Limit Accepted Range
        if(speed < -100):
            speed = -100
        if(speed > 100):
            speed = 100

        LFWSpeed = speed + strafe + turn
        LBWSpeed = speed - strafe + turn
        RFWSpeed = speed - strafe - turn
        RBWSpeed = speed + strafe - turn

        pwmENAA = GPIO.PWM(self.ENAA, 25000)
        pwmENAB = GPIO.PWM(self.ENAB, 25000)
        pwmENBA = GPIO.PWM(self.ENBA, 25000)
        pwmENBB = GPIO.PWM(self.ENBB, 25000)

        pwmENAA.start(RBWSpeed)
        pwmENAB.start(RFWSpeed)
        pwmENBA.start(LFWSpeed)
        pwmENBB.start(LBWSpeed)

        GPIO.output(self.INA1, 1)
        GPIO.output(self.INA2, 0)
        GPIO.output(self.INA3, 1)
        GPIO.output(self.INA4, 0)

        GPIO.output(self.INB1, 1)
        GPIO.output(self.INB2, 0)
        GPIO.output(self.INB3, 1)
        GPIO.output(self.INB4, 0)


############################

def main():
    # GPIO PIN CONFIG
    print("This is main() !!!")

    #RBW
    ENAA=37
    INA1=35
    INA2=33

    #RFW
    ENAB=21
    INA3=31
    INA4=23

    #LFW
    ENBA=24
    INB1=32
    INB2=26

    #LBW
    ENBB=40
    INB3=38
    INB4=36

    lions = L298N(ENAA, INA1, INA2, ENAB, INA3, INA4, ENBA, INB1, INB2, ENBB, INB3, INB4)

    speed  = 100
    strafe = 0
    turn   = 0
    lions.drive(speed, strafe, turn)

    time.sleep(25)

#############################################

# TEST CODE
if __name__=="__main__":
    #RBW
    ENAA=37
    INA1=35
    INA2=33

    #RFW
    ENAB=21
    INA3=31
    INA4=23

    #LFW
    ENBA=24
    INB1=32
    INB2=26

    #LBW
    ENBB=40
    INB3=38
    INB4=36

    count = 100
    try:
        print("Trying to PWM......")

        while count > 0:
            print(f"Count Pre:  {count}")
            # main()

            # BUG:  FOLLOWING TWO LINES ARE SKIPPED, ENDING PREMATURELY ???
            # count -= 1
            # print(f"Count Post:  {count}")


            ## ALL DRIVE
            # lions = L298N(ENAA, INA1, INA2, ENAB, INA3, INA4, ENBA, INB1, INB2, ENBB, INB3, INB4)

            # speed  = 100
            # strafe = 0
            # turn   = 0
            # lions.drive(speed, strafe, turn)

            # time.sleep(20)


            ## RBW DRIVE
            rightBack = L298N(ENAA, INA1, INA2, ENAB, INA3, INA4, ENBA, INB1, INB2, ENBB, INB3, INB4)
            rightBack.drive()

            time.sleep(20)

            print("Right Back Wheel: FWD ?")


            count -= 1




    except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
       print("Keyboard interrupt")

    except:
       print("Some Error") 

    finally:
       print("Clean Up") 
       GPIO.cleanup() # cleanup all GPIO 


############

'''
    --BUG REPORT--
    Battery power somehow bypasses software ON/OFF constraints and activates
    ONLY the Left-Front Wheel (LFW, PWM pin ENBA of motor controller).


'''