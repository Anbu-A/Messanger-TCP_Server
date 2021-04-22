import sys
from server import Server

# symbolical constants;
PORT        = 9999
SERVER      = "127.0.0.1"


def Main():
    with Server(SERVER, PORT) as server:
        server.start_server() 


if __name__ == '__main__':
    Main()
