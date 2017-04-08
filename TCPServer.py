import socket, threading

bind_ip = "0.0.0.0"
bind_port = 9999

# AF_INET means that it is using ipv4, and SOCK_STREAM means that it is using tcp
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Tell the server to start listening
server.bind((bind_ip, bind_port))

#Maximum backlog connections of 5
server.listen(5)

print '[*] Listening on %s:%d' % (bind_ip, bind_port)

# this is our client-handling thread
def handle_client(client_socket):

    #print out what the client sends
    request = client_socket.recv(1024)

    print '[*] Recieved %s' % request

    #send back a packet
    client_socket.send('ACK!')

    client_socket.close()

#main loop, waiting for an incoming connection
while True:

    #the loop waits here until server.accept is called, because otherwise it cannot
    #assign client and addr
    
    client,addr = server.accept()

    #prints out the ip and port of the incoming connection
    print '[*] Accepted connection from %s:%d' % (addr[0],addr[1])

    #spin up our client thread to handle incoming data,
    #which then creates a thread which calls handle_client and passes the client as a parameter 
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
