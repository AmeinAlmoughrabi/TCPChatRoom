import threading 
import socket

# these are the two modules we are going to use

# defining a host and port
host = "127.0.0.1" # localhost
port = 5555

# now we want to start a server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# internet socket, stream socket, TCP
server.bind((host, port))
# bind the host and port
server.listen(5)
# listen for 5 connections, listens for incoming connections

clients = []
# this is a list of clients
screenNames = []
# this is a list of screen names


# we will define broadcast function, handle method, and receive method
    # broadcast function will send a message to all clients
    # handle function will handle the incoming messages from clients and send them back to clients
    # receive function will receive messages from clients that will combine all previous methods

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            screenName = screenNames[index]
            print("Client {} disconnected".format(screenName[index]))
            screenNames.remove(screenName)
            break

# try to receive messages from clients of 1024 bytes
# if there is a message and it succeeds, broadcast it to all clients
# Else, cut the connection with the client and remove it from the list of clients, as well as terminate the loop
# let the client know that they have disconnected and broadcast the message to all clients

# each client will have a thread running in a loop
# this will run in a loop until the client disconnects

def receive():
    while True:
        client, address = server.accept()
        print("Client connected from {}".format(address))
        client.send("screenName".encode("utf-8"))
        screenName = client.recv(1024).decode("utf-8")
        clients.append(client)
        screenNames.append(screenName)
        print("Client {} connected".format(screenName))
        broadcast(f'{screenName} has joined the chat!'.encode("utf-8"))
        client.send("Welcome to the chat!".encode("utf-8"))
        
        thread = threading.Thread(target=handle, args=(client,))
        # now we are going to run a thread for each client
        # this is to avoid overlap and process it at the same time
        thread.start()
        # this will start the thread



# if this method gets a connection it will return a client and the address of the client
    # useful if running on a server
# we want to ask the client for their screen name
    # we will send the client a message to ask for their screen name
    # we will receive the screen name from the client
    # we will add the screen name to the list of screen names
    # we will broadcast the screen name to all clients

print("Server started on port {}".format(port))
receive()


# summarize this code in a sentence:
# the server will start listening for connections
# when a client connects, the server will accept the connection
# the server will send the client a message to ask for their screen name
# the server will receive the screen name from the client
