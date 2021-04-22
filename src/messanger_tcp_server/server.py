# librarys
import socket
from _thread import *

class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.buffer_size = 1024
        self.connected_clients = []
        self.client_names = {} 

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
            msg = "[System]: Thank you for connecting\n"    
            client.send(msg.encode())
    
            start_new_thread(self.new_con, (client, addr, ))


    def new_con(self, client, addr):
        self.connected_clients.append(client)
        client_name = client.recv(self.buffer_size).decode()
        self.client_names[client] = client_name
        print(client_name)

        while True:
            while(True):
                client_msg = client.recv(self.buffer_size).decode()
                print(f"User {str(client_name)}: {client_msg}")

                for clients in self.connected_clients:
                    if(clients != client):  
                        clients.send((f"[{client_name}]:{client_msg}\n").encode())                
                break
