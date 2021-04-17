# librarys
import socket
from _thread import *


# symbolical constants
BUFFER_SIZE = 1024
PORT        = 9999
SERVER      = "127.0.0.1"


# global variables
CONNECTED_CLIENTS = []
CLIENT_NAMES = {} 


# function for threading
# handles messages from client,
# every client has its own thread with this function
def new_con(client, addr):
    # add new clients to list and creates dict entry with name(which is the first message to receive from the client)
    CONNECTED_CLIENTS.append(client)
    client_name = client.recv(BUFFER_SIZE).decode()
    CLIENT_NAMES[client] = client_name
    print(client_name)

    while True:
        while(True):
            client_msg = client.recv(BUFFER_SIZE).decode()
            print(f"User {str(client_name)}: {client_msg}")
            
            # server receives message from a client and send it 
            # to all other connected clients 
            for clients in CONNECTED_CLIENTS:
                if(clients != client):  
                    clients.send((f"[{client_name}]:{client_msg}\n").encode())                
            break


# source: https://www.geeksforgeeks.org/socket-programming-python/
def Main():
    # next create a socket object
    s = socket.socket()		
    print ("Socket successfully created")

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', PORT))		
    print ("socket binded to %s" %(PORT))

    # put the socket into listening mode
    s.listen(5)	
    print ("socket is listening")			

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        client, addr = s.accept()

        print ('Got connection from', addr )
        # send a thank you message to the client.
        msg = "thank you for connecting\n"
   
        #client.send('Thank you for connecting')
        client.send(msg.encode())

        # starts new thread
        start_new_thread(new_con, (client, addr, ))

        # Close the connection with the client
        #client.close()

if __name__ == '__main__':
    Main()