import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    # Send data
    f= open("test.txt","rb")
    l= f.read(1024)
    print(f"sending {l}")
    # Look for the response
    while (l):
        sock.send(l)
        l= f.read(1024)
finally:
    print("closing")
    sock.close()