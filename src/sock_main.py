from websocket import WebSockServer

def handleMessage(msg, data):
	print("Incoming", msg, data)

server = WebSockServer(handleMessage)

server.run()
