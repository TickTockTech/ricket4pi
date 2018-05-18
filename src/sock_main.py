from websocket import WebSockServer
import movement as move
import robohat
from messages import Messages

robohat.init()
move.init()

def jsonBool(boole):
    if boole:
        return "true"
    else:
        return "false"

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
    elif msg == Messages.MSG_FORWARD:
        print "Forward!"
        move.forward(2, 30)
    else:
        print "[WARN] Not handled!"

server = WebSockServer(handleMessage)

server.run()
