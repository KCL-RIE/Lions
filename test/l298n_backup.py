import RPi.GPIO as GPIO
import time


class L298N:
    """A class to control one side of an L298N dual H bridge motor driver with speed control."""

    def __init__(self, ena, in1, in2):
        self.in1 = in1
        self.in2 = in2
        self.ena = ena
        all_pins = [self.ena, self.in1, self.in2]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(all_pins, GPIO.OUT)
        GPIO.setwarnings(False)

    def forward(self, speed=100):
        pwm = GPIO.PWM(self.ena, 800)

        print("forward():  Run pwm start.")
        pwm.start(speed)
        print("forward():  Ran pwm start.")

        print("forward():  Run GPIO output.")
        GPIO.output(self.in1, 1)
        GPIO.output(self.in2, 0)

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


# def moveRightBack(ENAA, INA1, INA2):
#     rightBack = L298N(ENAA, INA1, INA2)
#     rightBack.forward()

#     time.sleep(20)

#     print("Right Back Wheel: FWD ?")
#     count -= 1


# def moveAllWheels(ENAA, INA1, INA2, ENAB, INA3, INA4, ENBA, INB1, INB2, ENBB, INB3, INB4):
#     # Speed Limit Accepted Values
#     if(speed < -100):
#         speed = -100
#     if(speed > 100):
#         speed = 100

#     LFWSpeed = speed + strafe + turn
#     LBWSpeed = speed - strafe + turn
#     RFWSpeed = speed - strafe - turn
#     RBWSpeed = speed + strafe - turn

#     pwm = GPIO.PWM(self.ena, 800)
#     pwm.start(speed)
#     GPIO.output(self.in1, 1)
#     GPIO.output(self.in2, 0)


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

    count = 10
    try:
        print("Trying to PWM......")
        print("")

        while count > 0:
            print(f"While loop countdown: {count}.")
            rightBack = L298N(ENBB, INB3, INB4)

            ## BUG:  Below hangs, never executes...
            print("Run ENBB, INB3, INB4.")
            print("Run forward function.")
            rightBack.forward()
            print("Ran forward function.")

            print("Sleep start")
            time.sleep(20)

            print("Sleep end.")
            count -= 1

            GPIO.cleanup()

    except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
       print("Keyboard interrupt")

    except:
       print("Some Error") 

    finally:
       print("Clean Up") 
       GPIO.cleanup() # cleanup all GPIO 
