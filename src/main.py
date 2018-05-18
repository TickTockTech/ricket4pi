import os
import SimpleHTTPServer
import SocketServer

web_dir = os.path.dirname(os.path.abspath(__file__)) + "/../www/"
os.chdir(web_dir) 

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
