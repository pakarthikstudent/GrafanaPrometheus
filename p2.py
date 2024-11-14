import http.server
import time
from prometheus_client import start_http_server

from prometheus_client import Counter

REQ1 = Counter('hello_world_total','hello world is requested')
REQ2 = Counter('hello_world_result','serving helloworld')

class myclass(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		REQ.inc()
		self.send_response(200)
		self.wfile.write(b"Hello world")
		self.myblock()
	def myblock(self):
		REQ2.inc()
		for var in range(15):
			var=var+100
			time.sleep(2)

if __name__ == '__main__':
	start_http_server(8000)
	server = http.server.HTTPServer(('localhost',8001),myclass)
	server.serve_forever()