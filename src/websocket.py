from websocket_server import WebsocketServer
import logging
import json

class WebSockServer():
    def __init__(self, handler):
        PORT=8807
        self.server = WebsocketServer(PORT, host='0.0.0.0', loglevel=logging.DEBUG)
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received)
        self.handler = handler

    # Called for every client connecting (after handshake)
    def new_client(self, client, server):
        print("New client connected. id=%d" % client['id'])
        msg='{{"msg":1,"data":{{"id":{0}}}}}'.format(client['id'])
        print("-> " +  msg)
        self.server.send_message_to_all(msg)


    # Called for every client disconnecting
    def client_left(self, client, server):
        print("Client(%d) disconnected" % client['id'])
        msg='{{"msg":2,"data":{{"id":{0}}}}}'.format(client['id'])
        print("-> " +  msg)
        self.server.send_message_to_all(msg)

    # Called when a client sends a message
    def message_received(self, client, server, message):
        if len(message) > 200:
            message = message[:200]+'..'
        print("id #%d <- %s" % (client['id'], message))

        # TODO: Handle invalid messages
        incoming = json.loads(message)

        if 'data' in incoming:
            self.handler(incoming["msg"], incoming["data"])
        else:
            self.handler(incoming["msg"], None)

    def send(self, msg):
        self.server.send_message_to_all(msg)

    def run(self):
        self.server.run_forever()

