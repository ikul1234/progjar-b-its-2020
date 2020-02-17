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
    with open('test.txt', 'wb') as f:
        print("file opened")
        while True:
            print("receiving data...")
            data = sock.recv(1024)
            print('data= %s', (data))
            f.write(data)
            if not data:
                f.close()
                break
finally:
    print("closing")
    sock.close()