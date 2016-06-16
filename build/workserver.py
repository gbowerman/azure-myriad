# workserver.py - simple HTTP server with a do_work / stop_work API
# GET /do_work activates a worker thread which uses CPU
# GET /stop_work signals worker thread to stop
import math
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = socket.gethostname()
hostPort = 9000

keepWorking = False  # boolean to switch worker thread on or off


# thread which maximizes CPU usage while the keepWorking global is True
def workerThread():
    # outer loop to run while waiting
    while (True):
        # main loop to thrash the CPI
        while (keepWorking == True):
            for x in range(1, 69):
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


# HTTP server response
def httpResponse(self, retCode, body):
    standardResponse(self, retCode)
    responseString = '<html><head><title>Work interface</title></head>'
    responseString += '<body><h2>Worker interface on ' + hostName + '</h2><ul><h3>'
    responseString += body
    responseString += '</h3></ul></body></html>'
    webOut(self, responseString)


# web API for switching on and off workload
class workServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global keepWorking
        if self.path == '/do_work' or self.path == '/do_work/':
            # start worker thread
            keepWorking = True
        elif self.path == '/stop_work' or self.path == '/stop_work/':
            # stop worker thread
            keepWorking = False
        elif self.path != '/':
            body = '<br/>URI not found:  ' + self.path + '<br/>'
            httpResponse(self, 404, body)
            return
        if keepWorking == False:
            body = '<br/>Worker thread is not running. <a href="./do_work">Start work</a><br/>'
        else:
            body = '<br/>Worker thread is running. <a href="./stop_work">Stop work</a><br/>'
        body += '<br/>Usage:<br/><br/>/do_work = start worker thread<br/>/stop_work = stop worker thread<br/>'
        httpResponse(self, 200, body)


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
