# workserver.py - simple HTTP server with a do_work / stop_work API
# GET /do_work activates a worker thread which uses CPU
# GET /stop_work signals worker thread to stop
from http.server import BaseHTTPRequestHandler, HTTPServer
import math
import socket
import threading
import time

hostName = socket.gethostname()
hostPort = 9000

keepWorking = False  # boolean to switch worker thread on or off

# thread which maximizes CPU usage while the keepWorking global is True
def workerThread():
    # outer loop to run while waiting
    while(True):
        # main loop to thrash the CPI
        while(keepWorking == True):
            for x in range(1,69):
                y = math.factorial(x)
        time.sleep(3)

# send a standard web header
def standardResponse(self, code):
    self.send_response(code)
    self.send_header("Content-type", "text/html")
    self.end_headers()

# write a string to http server in UTF-8 bytes
def webOut(self, outStr):
    self.wfile.write(bytes(outStr, 'utf-8'))

# web API for switching on and off workload
class workServer(BaseHTTPRequestHandler):      
    def do_GET(self):
        global keepWorking
        if self.path == '/do_work' or self.path == '/do_work/':
            # start worker thread
            keepWorking = True
            standardResponse(self, 200)
            webOut(self, '<html><head><title>Work started</title></head>')
            webOut(self, '<p>Worker thread started.</p>')
        elif self.path == '/stop_work' or self.path == '/stop_work/':
            # stop worker thread
            keepWorking = False
            standardResponse(self, 200)
            webOut(self, '<html><head><title>Work stopped</title></head>')
            webOut(self, '<p>Worker thread stopped.</p>')
        elif self.path == '/':           
            standardResponse(self, 200)
            webOut(self, '<html><head><title>Work interface</title></head>')
            webOut(self, '<body><h2>Worker interface: ' + hostName + '</h2><p>Usage:</p>')
            webOut(self, '<p>/do_work = start worker thread<br/>/stop_work = stop worker thread</p>')            
        else:
            standardResponse(self, 404)
            webOut(self, '<html><head><title>Not found</title></head>')
            webOut(self, '<body><p>URI not found:  ' + self.path + '</p>')
        webOut(self, '</body></html>')

# start the worker thread
worker_thread = threading.Thread(target=workerThread, args=())
worker_thread.start()

# start http server
# bind to any hostname (otherwise put hostName in 1st argument)
workServerInst = HTTPServer(('', hostPort), workServer)
print(time.asctime(), "Server Started - %s:%s" % (hostName, hostPort))
try:
    workServerInst.serve_forever()
except KeyboardInterrupt:
    pass
# stop http server
workServerInst.server_close()
print(time.asctime(), "Server Stopped - %s:%s" % (hostName, hostPort))
