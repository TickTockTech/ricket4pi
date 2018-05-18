# initio Servo Test using simple PWM
# Do not expect this to be reliable or stable
# Moves the servo left, centre, right and repeats
# Press Ctrl-C to stop
#
# Please use servoTest.py for correct operation
#
# Run using: sudo python servoTest.py


import time, RPi.GPIO as gpio

YAW_SERVO_PIN = 22
YAW_SERVO_LEFT = 50/5
YAW_SERVO_RIGHT = 250/5
YAW_SERVO_MID = 150/5

class ServoYaw:
    def __init__(self):
        gpio.setup(YAW_SERVO_PIN, gpio.OUT)

        self.pwm = gpio.PWM(YAW_SERVO_PIN, 200)   # frequency is 500Hz, so each pulse is 5ms wide
        # servos will be fully left at 0.5ms, centred at 1.5ms and fully right at 2.5ms

        self.pwm.start(YAW_SERVO_MID)
        time.sleep(1)
        self.pwm.stop()

        print "ServoYaw on pin:", YAW_SERVO_PIN
        print

    def mid(self):
        self.pwm.start(YAW_SERVO_MID)
        time.sleep(1)
        self.pwm.stop()

    def left(self):
        self.pwm.start(YAW_SERVO_LEFT)
        time.sleep(1)
        self.pwm.stop()

    def right(self):
        self.pwm.start(YAW_SERVO_RIGHT)
        time.sleep(1)
        self.pwm.stop()
