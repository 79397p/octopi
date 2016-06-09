#I want to spend my summer having fun creating. For that reason I decided to just base this on something familiar (my socket programming assignments from NTNU).

# Import socket module
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# FILL IN START

# Assign a port number
serverPort = 12000

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print 'ready to serve'

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filepath = message.split()[1] #handles GET <url> HTTP/<version_number>

        f = open(filepath[1:])
        outputdata = f.read()
        f.close()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")
        connectionSocket.close()

    except IOError:
        print 'Error: NotFound'
        connectionSocket.send('HTTP/1.1 404 NotFound\r\n\r\n')
        connectionSocket.send("<html><head></head><body><h1>404 NotFound</h1></body></html>\r\n")

        connectionSocket.close()

serverSocket.close()
