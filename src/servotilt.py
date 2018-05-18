# initio Servo Test using simple PWM
# Do not expect this to be reliable or stable
# Moves the servo left, centre, right and repeats
# Press Ctrl-C to stop
#
# Please use servoTest.py for correct operation
#
# Run using: sudo python servoTest.py


import time, RPi.GPIO as gpio

TILT_SERVO_PIN = 18
DIR_SERVO_UP = 20
DIR_SERVO_DOWN = 30
DIR_SERVO_LOW = 35
DIR_SERVO_CENTRE = 25

TILT_FREQ = 200

# Assumed done in robothat.py
# gpio.setmode(gpio.BOARD)

class ServoTilt:
    def __init__(self):
        gpio.setup(TILT_SERVO_PIN, gpio.OUT)
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)   # frequency is 500Hz, so each pulse is 5ms wide
        # servos will be fully left at 0.5ms, centred at 1.5ms and fully right at 2.5ms

        self.pwm.start(DIR_SERVO_CENTRE) # start it at 50% - should be centre of servo
        time.sleep(1)
        self.pwm.stop()

        print "ServoTilt on pin:", TILT_SERVO_PIN

    def centre(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_CENTRE)
        print 'TiltServo - Centre'
        time.sleep(2)
        self.pwm.stop()

    def up(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_UP)
        print 'TiltServo - Up'
        time.sleep(2)
        self.pwm.stop()

    def down(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_DOWN)
        print 'TiltServo - Down'
        time.sleep(2)
        self.pwm.stop()

    def low(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_LOW)
        print 'TiltServo - Low'
        time.sleep(2)
        self.pwm.stop()
