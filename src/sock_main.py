from websocket import WebSockServer
import movement as move
import robohat
from messages import Messages
from servoyaw import ServoYaw
from servotilt import ServoTilt

robohat.init()
move.init()

def jsonBool(boole):
    if boole:
        return "true"
    else:
        return "false"

def sonarScan(self):
    yaw.left()
    tilt.up()
    uL = robohat.getDistance()

    yaw.mid()
    uM = robohat.getDistance()

    yaw.right()
    uR = robohat.getDistance()

    tilt.centre()
    cR = robohat.getDistance()

    yaw.mid()
    cM = robohat.getDistance()

    yaw.right()
    cL = robohat.getDistance()

    tilt.down()
    dR = robohat.getDistance()

    yaw.mid()
    dM = robohat.getDistance()

    yaw.left()
    dL = robohat.getDistance()

    tilt.low()
    lR = robohat.getDistance()

    yaw.mid()
    lM = robohat.getDistance()

    yaw.right()
    lL = robohat.getDistance()

    yaw.mid()
    tilt.centre()

    msg='{{"msg":{0},"data":{[[{1},{2},{3}],[{4},{5},{6}],[{7},{8},{9}],[{10},{11},{12}]]}}';
    msg = msg.format(Messages.MSG_SONAR_SCAN_DATA, uL, uM, uR, cL, cM, cR, dL, dM, dR, lL, lM, lR)
    server.send(msg)

def handleMessage(msg, data):
    global server

    print("Incoming", msg, data)

    if msg == Messages.MSG_READ_SENSORS:
        irL = jsonBool( robohat.irLeft() )
        irR = jsonBool( robohat.irRight() )
        lineL = jsonBool( robohat.irLeftLine() )
        lineR = jsonBool( robohat.irRightLine() )
        sonar = robohat.getDistance()

    if msg == Messages.MSG_READ_SENSORS:
        msg='{{"msg":{0},"data":{{"irL":{1},"irR":{2},"lineL":{3},"lineR":{4},"dist":{5}}}}}';
        msg = msg.format(Messages.MSG_SENSOR_DATA, irL, irR, lineL, lineR, sonar)
        server.send(msg)
    elif msg == Messages.MSG_FORWARD or msg == Messages.MSG_REVERSE:
        revs = 2
        speed = 40
        if data != None:
            if data.r != None:
                revs = data.r
            if data.s != None:
                speed = data.s
        if msg == Messages.MSG_FORWARD:
            print "Forward!"
            move.forward(revs, speed)
        else:
            print "Reverse!"
            move.reverse(revs, speed)
    elif msg == Messages.MSG_LEFT or msg == Messages.MSG_RIGHT:
        revs = 0.5
        speed = 100
        if data != None:
            if data.r != None:
                revs = data.r
            if data.s != None:
                speed = data.s
        if msg == Messages.MSG_LEFT:
            print "Left!"
            move.left(revs, speed)
        else:
            print "Right!"
            move.right(revs, speed)
    elif msg == Messages.MSG_SONAR_UP:
        print "Sonar up!"
        tilt.up()
    elif msg == Messages.MSG_SONAR_CENTRE:
        print "Sonar centre!"
        tilt.centre()
    elif msg == Messages.MSG_SONAR_DOWN:
        print "Sonar down!"
        tilt.down()
    elif msg == Messages.MSG_SONAR_LOW:
        print "Sonar low!"
        tilt.low()
    elif msg == Messages.MSG_SONAR_MID:
        print "Sonar middle!"
        yaw.mid()
    elif msg ==Messages. MSG_SONAR_LEFT:
        print "Sonar left!"
        yaw.left()
    elif msg == Messages.MSG_SONAR_RIGHT:
        print "Sonar right!"
        yaw.right()
    if msg == Messages.MSG_SONAR_SCAN:
        sonarScan()
    if msg == Messages.MSG_PARK_SONAR:
        yaw.mid()
        tilt.park()
    else:
        print "[WARN] Not handled!"

server = WebSockServer(handleMessage)
tilt = ServoTilt()
yaw = ServoYaw()

server.run()
