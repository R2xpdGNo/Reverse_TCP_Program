# Reverse_TCP_Program
Reverse TCP program written in python.

This program is a work in progress, I will continue to update the code as much as I can. I will create executable files for each python file to make it easier to use.

## Setup

**Client.py**

Host: IP address of the Server. This could be an internal address, such as 192.168.xxx.xxx, or external address
Port: Choose whatever port you wish to open a tcp connection on. Make sure "Client.py" port is the same as your "Server.py" port.

***Server.py***

SERVER_HOST: IP address of the machine you are running this program on. It must be your internal address
SERVER_PORT: Choose whatever port you wish to open a tcp connection on. Make sure "Client.py" port is the same as your "Server.py" port.

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

any file downloaded or uploaded will be downloaded/uploaded in the same directory of the client or server file

**Setup**

No additional setup required

## Contact
Feel Free to email me with any questions:
R2xpdGNo@proton.com

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
