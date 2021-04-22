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

class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __enter__(self) :
        return self
    
    def __exit__ (self, exception_type, exception_value, traceback):
        print("DC")
        #client.close()

    def start_server(self):
        s = socket.socket()		
        print ("Socket successfully created")
    
        s.bind(('', PORT))		
        print ("socket binded to %s" %(PORT))
    
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
        

def Main():
    with Server(SERVER, PORT) as server:
        server.start_server()


if __name__ == '__main__':
    Main()
