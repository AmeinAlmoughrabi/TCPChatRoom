import socket 
import threading


screenName = input("Enter your screen name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))
# now instead of binding the client to a port we will connect it to a port

# now the server will trigger the method and the client is now connected to the server

# now we will define 2 methods and threads 
# one method will be to receive messages from the client
# the other will be to send messages to the client

def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == 'screenName':
                client.send(screenName.encode("utf-8")) 
                pass
            # this will check if the message is 'screenName' and if it is, it will send the screen name to the sever
            else:

                print(message)
        except:
            print ("Client disconnected, an error occured")
            client.close()
            break



def write():
    while True:
        message = f'{screenName}: {input("")}'
        # we are constantly running new input functions
        # as soona as someone types in a message, it will be sent to the server
        # the user can only send new messages or close the program
        client.send(message.encode("utf-8"))
        # this will send the message to the server and the server will send it to the client

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
# this will start the threads
# the threads will run the methods in parallel
# the threads will run until the program is closed
