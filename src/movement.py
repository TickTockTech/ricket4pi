import RPi.GPIO as GPIO, sys, threading, time, os, subprocess
import robohat

CLICKS_PER_REV = 36

class MotorSensor:

    def __init__(self, sensorPin):
        self._sensorClicks = 0
        self._targetClicks = 0
        self._reachedTarget = threading.Event()
        GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(sensorPin, GPIO.RISING, callback=self._sensorCallback, bouncetime=2)

    def start(self, targetClicks):
        self._sensorClicks = 0
        self._targetClicks = targetClicks
        self._reachedTarget.clear()
        return self._reachedTarget

    def _sensorCallback(self, pin):
        self._sensorClicks += 1
        if (self._sensorClicks >= self._targetClicks):
            self._reachedTarget.set()

SENS_L = 0
SENS_R = 1

def init():
    global sensors
    # sensorPin: in Scratch these are 7 and 11. On robohat wires connect to 15 and 16,
    # which are connect to the same gpio pins, see https://4tronix.co.uk/blog/?p=1196
    sensors = [ MotorSensor(15), MotorSensor(16) ]

# revs: number of wheel turns, float.
def forward(revs, speed):
    robohat.forward(speed)

    clicks = int(revs*CLICKS_PER_REV)
    # doesn't matter which side's sensor we use
    s = sensors[SENS_L]
    s.start(clicks).wait(5)

    # TODO: figure out how many clicks for the motors to stop, and allow for that
    # in the above loop:
    # speed, extra clicks
    # 30, 7-8
    # 50, 11-12
    # 70, 13
    # 100, 13-14
    robohat.stop()

    time.sleep(1)
    print("final clicks: ", s._sensorClicks)

# revs: number of wheel turns, float.
def findWall(speed):
    s = sensors[SENS_R]
    sClicks = s._sensorClicks
    robohat.forward(speed)
    # Sanity check (possibly report timeout)
    countDown = 1000

    while(not robohat.irAll() and countDown > 0):
        time.sleep(0.01)
        countDown -= 1

    robohat.stop()

    time.sleep(1)
    eClicks = s._sensorClicks
    print("final clicks: ", (sClicks - eClicks))

# revs: number of wheel turns, float.
def reverse(revs, speed):
    robohat.reverse(speed)

    clicks = int(revs*CLICKS_PER_REV)
    # doesn't matter which side's sensor we use
    s = sensors[SENS_L]
    s.start(clicks).wait(5)

    robohat.stop()

    time.sleep(1)
    print("final clicks: ", s._sensorClicks)

# revs: number of wheel turns, float.
def left(revs, speed):
    robohat.spinLeft(speed)

    clicks = int(revs*CLICKS_PER_REV)
    # doesn't matter which side's sensor we use
    s = sensors[SENS_L]
    s.start(clicks).wait(5)

    robohat.stop()

    time.sleep(1)
    print("final clicks: ", s._sensorClicks)

# revs: number of wheel turns, float.
def right(revs, speed):
    robohat.spinRight(speed)

    clicks = int(revs*CLICKS_PER_REV)
    # doesn't matter which side's sensor we use
    s = sensors[SENS_L]
    s.start(clicks).wait(5)

    robohat.stop()

    time.sleep(1)
    print("final clicks: ", s._sensorClicks)

def getClicks():
    s = sensors[SENS_L]
    return s._sensorClicks

def resetClicks():
    s = sensors[SENS_L]
    s._sensorClicks = 0
