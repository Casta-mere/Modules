from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

data = {'result': 'Welcome to Castamere'}

class httpServer:
    
    def __init__(self):
        os.system("clear")
        self.initHostInfo()

    def initHostInfo(self):
        config = json.load(open('config.json', 'r'))
        self.inner_ip = config['server_inner_ip']
        self.outer_ip = config['server_outer_ip']
        self.port = config['server_port']
        self.host = (self.inner_ip, self.port)
    
    def startServer(self):
        self.server = HTTPServer(self.host, self.Resquest)
        print("Starting server, listen at:")
        print("inner_ip: %s" % self.inner_ip)
        print("outer_ip: %s" % self.outer_ip)
        print("port: %s" % self.port)
        self.server.serve_forever()

    def stopServer(self):
        self.server.socket.close()

    class Resquest(BaseHTTPRequestHandler):

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        def do_POST(self):
            datas = self.rfile.read(int(self.headers['content-length']))

            print('headers', self.headers)
            print("do post:", self.path, self.client_address, datas)
    
if __name__ == '__main__':
    http_server = httpServer()
    http_server.startServer()
