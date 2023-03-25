import RPi.GPIO as GPIO
import time

# Motor controller pin definitions
enable_pin = 33
in1_pin = 35
in2_pin = 37

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

# Set up PWM for the enable pin
pwm = GPIO.PWM(enable_pin, 1000)

# Start the PWM with a duty cycle of 0
pwm.start(0)

try:
    while True:
        # Set the motor to spin forward at maximum speed
        GPIO.output(in1_pin, GPIO.HIGH)
        GPIO.output(in2_pin, GPIO.LOW)
        pwm.ChangeDutyCycle(100)

        # Wait for 5 seconds
        time.sleep(5)

        # Set the motor to spin backward at half speed
        GPIO.output(in1_pin, GPIO.LOW)
        GPIO.output(in2_pin, GPIO.HIGH)
        pwm.ChangeDutyCycle(50)

        # Wait for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    # Clean up GPIO and exit on Ctrl+C
    GPIO.cleanup()