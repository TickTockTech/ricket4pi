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
YAW_SERVO_LEFT = 40
YAW_SERVO_RIGHT = 20
YAW_SERVO_MID = 30

YAW_FREQ = 200
YAW_DELAY = 1.5
YAW_PAUSE = 0.25

class ServoYaw:
    def __init__(self):
        gpio.setup(YAW_SERVO_PIN, gpio.OUT)

        self.pwm = gpio.PWM(YAW_SERVO_PIN, YAW_FREQ)   # frequency is 500Hz, so each pulse is 5ms wide
        # servos will be fully left at 0.5ms, centred at 1.5ms and fully right at 2.5ms

        self.pwm.start(YAW_SERVO_MID)
        time.sleep(YAW_DELAY)
        self.pwm.stop()
        time.sleep(YAW_PAUSE)

        print "ServoYaw on pin:", YAW_SERVO_PIN
        print

    def mid(self):
        self.pwm = gpio.PWM(YAW_SERVO_PIN, YAW_FREQ)
        self.pwm.start(YAW_SERVO_MID)
        time.sleep(YAW_DELAY)
        self.pwm.stop()
        time.sleep(YAW_PAUSE)

    def left(self):
        self.pwm = gpio.PWM(YAW_SERVO_PIN, YAW_FREQ)
        self.pwm.start(YAW_SERVO_LEFT)
        time.sleep(YAW_DELAY)
        self.pwm.stop()
        time.sleep(YAW_PAUSE)

    def right(self):
        self.pwm = gpio.PWM(YAW_SERVO_PIN, YAW_FREQ)
        self.pwm.start(YAW_SERVO_RIGHT)
        time.sleep(YAW_DELAY)
        self.pwm.stop()
        time.sleep(YAW_PAUSE)

    def percentage(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        value = 100 - value
        range = float(YAW_SERVO_LEFT - YAW_SERVO_RIGHT)

        d = (range / 100) * value

        pos = int(YAW_SERVO_RIGHT + d)

        self.pwm = gpio.PWM(YAW_SERVO_PIN, YAW_FREQ)
        self.pwm.start(pos)
        print 'YawServo - yaw',pos,'%'
        time.sleep(YAW_DELAY)
        self.pwm.stop()
        time.sleep(YAW_PAUSE)
