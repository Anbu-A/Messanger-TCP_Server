====================
Messenger-TCP_Server
====================


Creates a socket and binds it to chosen port.
Clients can then connect via said ip and port.
Messages received by the clients are then redirected to all other connected clients.  


Description
===========

Programm takes two arguments, the first for the ip and the second one for the port.
Then creates a socket with the Server class and the member function start_server() and binds it to chosen port.
Programm is then listening on this socket.

Clients can then connect via said ip and port.
If they do so a new socket object is being returned and additionally a tuple with the adress of the client (host , port)
After that the server sends a welcome message via the new socket object. 
-> The string first has to be encoded with encode() and is later being decoded at the client side

Now there will be created a new thread with the function new_con(), which takes the new socket object and adress as parameters.
The client is added to a list of connected clients.
In this thread the socket object client is receiving messages and is decoding them into strings with decode().
The first message received is being saved as the username.
A new dictionary entry for the dictionary holding the clientnames is being generated.

For all other messages:
The message is then being redirected to all other connected clients.


..code-block:: none
<test --help>