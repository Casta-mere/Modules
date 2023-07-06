# implemented by Castamere

import socket
import time

def get_self_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Client:

    def __init__ (self,ip=get_self_ip(),host=8888):
        self.ip = ip
        self.host = host
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect_server(self):
        count_retries = 0
        while True:
            try:
                self.client_socket.connect((self.ip,self.host))
                print(f"Connected to {self.ip}:{self.host}")
                break
            except:
                count_retries += 1
                if count_retries > 5 : break
                print(f"Connection to {self.ip}:{self.host} failed, retrying...")
                time.sleep(5)

    def is_connected(self):
        try:
            self.client_socket.send(b"")
            return True
        except:
            return False

        

    