#TCPClient.py
import socket

target_host = "0.0.0.0"
target_port = 9999

#create a socket object
# AF_INET paraameter means that we are using a standard IPv4 address or hostname
# SOCK_STREAM means that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host, target_port))

#send some data
client.send("ABCDEF")

#recieve some data
response = client.recv(4096)

print response
