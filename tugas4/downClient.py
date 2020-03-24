import socket
import sys
import base64
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)


requestfile = "george.jpg"
request = (b"download "+requestfile.encode())
print("Downloading file "+request.decode()+"...")
f = open(requestfile,"wb")
file =(b"")
sock.send(request)
data = sock.recv(1024)
while True:
    file = file + data
    print(data)
    if sys.getsizeof(data) != 1057:
        break
    else :
        data = sock.recv(1024)


file = base64.decodestring(file)

f.write(file)
f.close()
f = open("dir/george.jpg","rb")
f.close()
print("file "+requestfile+"Success Download")
sock.close()
