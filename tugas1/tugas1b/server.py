import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    f=open("test.txt","rb")
    data =f.read(1024)
    # Receive the data in small chunks and retransmit it
    while (data):
        connection.send(data)
        data=f.read(1024)
    f.close()
    print("Done")
    # Clean up the connection
    connection.close()