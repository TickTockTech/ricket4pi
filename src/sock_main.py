from websocket import WebSockServer
import movement as move
import robohat

MSG_

robohat.init()
move.init()

def handleMessage(msg, data):
	print("Incoming", msg, data)

	if msg == Messages.MSG_READ_SENSORS:
		print("* * * Read sensors")

server = WebSockServer(handleMessage)

server.run()
