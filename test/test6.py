#!/usr/bin/python3
# File name   : l298n.py
# Description : Control Mecanum Motors
# Author      : ChatGPT-4
# Date        : 2023/03/21


import RPi.GPIO as GPIO
import time

# Set the GPIO pins for the motors
#                 in1, in2, in3, in4, enA, enB
left_motor_pins  = [35, 33, 31, 29, 37, 23]
right_motor_pins = [38, 36, 32, 26, 40, 24]

# Ignore finnicky warnings
GPIO.setwarnings(False)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the left motor pins
GPIO.setup(left_motor_pins[0], GPIO.OUT)
GPIO.setup(left_motor_pins[1], GPIO.OUT)
GPIO.setup(left_motor_pins[2], GPIO.OUT)
GPIO.setup(left_motor_pins[3], GPIO.OUT)

# Set up the right motor pins
GPIO.setup(right_motor_pins[0], GPIO.OUT)
GPIO.setup(right_motor_pins[1], GPIO.OUT)
GPIO.setup(right_motor_pins[2], GPIO.OUT)
GPIO.setup(right_motor_pins[3], GPIO.OUT)

# Set the duty cycle to 50%
duty_cycle = 50

# Set the motors to move forward
left_motor_direction = [GPIO.HIGH, GPIO.LOW]
right_motor_direction = [GPIO.LOW, GPIO.HIGH]

# Set the motors to move forward at the specified duty cycle
GPIO.output(left_motor_pins[0], left_motor_direction[0])
GPIO.output(left_motor_pins[1], left_motor_direction[1])
GPIO.output(left_motor_pins[2], GPIO.HIGH)
GPIO.output(left_motor_pins[3], GPIO.LOW)

GPIO.output(right_motor_pins[0], right_motor_direction[0])
GPIO.output(right_motor_pins[1], right_motor_direction[1])
GPIO.output(right_motor_pins[2], GPIO.HIGH)
GPIO.output(right_motor_pins[3], GPIO.LOW)

left_motor_pwm1 = GPIO.PWM(left_motor_pins[4], 100)
left_motor_pwm2 = GPIO.PWM(left_motor_pins[5], 100)
right_motor_pwm1 = GPIO.PWM(right_motor_pins[4], 100)
right_motor_pwm2 = GPIO.PWM(left_motor_pins[5], 100)

left_motor_pwm1.start(duty_cycle)
left_motor_pwm2.start(duty_cycle)
right_motor_pwm1.start(duty_cycle)
right_motor_pwm2.start(duty_cycle)

try:
    while True:
        print("while loop running - until Error or KeyboardInterrupt")
        time.sleep(1)

except KeyboardInterrupt:
    print("Keyboard Interrupt!!!")

    left_motor_pwm1.stop()
    left_motor_pwm2.stop()
    right_motor_pwm1.stop()
    right_motor_pwm2.stop()

    GPIO.cleanup()