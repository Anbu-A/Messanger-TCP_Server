# librarys
import socket
from _thread import *


# global variables
CONNECTED_CLIENTS = []
CLIENT_NAMES = {} 

class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.buffer_size = 1024

    def __enter__(self) :
        return self
    
    def __exit__ (self, exception_type, exception_value, traceback):
        pass
        # will be used later on to dc

    def start_server(self):
        s = socket.socket()		
        print ("Socket successfully created")
    
        s.bind(('', self.port))		
        print ("socket binded to %s" %(self.port))
    
        s.listen(5)	
        print ("socket is listening")			
    
        while True:
            client, addr = s.accept()
    
            print ('Got connection from', addr )
            msg = "thank you for connecting\n"    
            client.send(msg.encode())
    
            start_new_thread(self.new_con, (client, addr, ))


    def new_con(self, client, addr):
        # add new clients to list and creates dict entry with name(which is the first message to receive from the client)
        CONNECTED_CLIENTS.append(client)
        client_name = client.recv(self.buffer_size).decode()
        CLIENT_NAMES[client] = client_name
        print(client_name)

        while True:
            while(True):
                client_msg = client.recv(self.buffer_size).decode()
                print(f"User {str(client_name)}: {client_msg}")

                # server receives message from a client and send it 
                # to all other connected clients 
                for clients in CONNECTED_CLIENTS:
                    if(clients != client):  
                        clients.send((f"[{client_name}]:{client_msg}\n").encode())                
                break
