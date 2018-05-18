import WebSocket

def handleMessage(msg, data):
	print("Incoming", msg, data)

server = WebSocket(handleMessage)

server.run()