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
DIR_SERVO_PARK = 5
DIR_SERVO_FLOOR = 40

TILT_FREQ = 200

TILT_DELAY = 1.5
TILT_PAUSE = 0.25

# Assumed done in robothat.py
# gpio.setmode(gpio.BOARD)

class ServoTilt:
    def __init__(self):
        gpio.setup(TILT_SERVO_PIN, gpio.OUT)
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)   # frequency is 500Hz, so each pulse is 5ms wide
        # servos will be fully left at 0.5ms, centred at 1.5ms and fully right at 2.5ms

        self.pwm.start(DIR_SERVO_CENTRE) # start it at 50% - should be centre of servo
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)

        print "ServoTilt on pin:", TILT_SERVO_PIN

    def centre(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_CENTRE)
        print 'TiltServo - Centre'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)

    def up(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_UP)
        print 'TiltServo - Up'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)

    def down(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_DOWN)
        print 'TiltServo - Down'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)

    def low(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_LOW)
        print 'TiltServo - Low'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)

    def park(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_PARK)
        print 'TiltServo - Park'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE) 

    def floor(self):
        self.pwm = gpio.PWM(TILT_SERVO_PIN, TILT_FREQ)
        self.pwm.start(DIR_SERVO_FLOOR)
        print 'TiltServo - Floor'
        time.sleep(TILT_DELAY)
        self.pwm.stop()
        time.sleep(TILT_PAUSE)
