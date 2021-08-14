# Reverse_TCP_Program
Reverse TCP program written in python.

This program is a work in progress, I will continue to update the code as much as I can. I will create executable files for each python file to make it easier to use. The program works by having the Client.py initiate a connection to the Server.py. Since the Client.py is initiating the connection the firewall allows the conneciton.

## Setup

**Client.py**

HOST: IP address of the Server. This could be an internal address, such as 192.168.xxx.xxx, or external address

PORT: Choose whatever port you wish to make a tcp connection on. Make sure the port in both "Client.py" and "Server.py" are the same

**Server.py**

SERVER_HOST: YOUR IP ADDRESS : internal address only

SERVER_PORT: Port you wish to host socket : if using external address, be sure to port forward

## List All Running Processes
List all runing proccesses on client maching and their corresponding pid

**Setup**

'pip install psutil'

'pip install pywin32'

## Screenshot
Take screenshot of client machine and send image back to server

**Setup**

'pip install pyautogui'

'pip install Pillow'

pyautogui is used to take screenshot
Pillow is used to read and save image bytes

## upload/download
upload and download any files between server and client

'upload  LOCATION OF FILE'

'download LOCATION  OF FILE'

Location of file must be exact locaiton, you cannot simply type 'filename.txt' instead you must give the exact path 'C:\users\username\Deckstop\filename.txt'

This will be changed soon.

**Setup**

No additional setup required

## Contact
Feel Free to email me with any questions: R2xpdGNo@proton.com

## TODO
- Add List Proccess (Done)
- Add Image sending client (Done)
- create class with all commands
- Find UAC Bypass (Done)
- Implement UAC Bypass into Client side code
- Find user to admin privilege escalation
- Implement user to admin privilege escalation
- Allow for Server to control multiple Clients
- add download/upload to move files between server and client (Done)
- mkdir / rmdir
- show system info
- shutdown/restart
- execute
- keep track of users current directory to allow for easy upload, download, mkdir, rmdir, and execute

## Disclaimer
These tools are provided for educational and research purposes only. The author of this project is in no way responsible for any misuse of these tools.
