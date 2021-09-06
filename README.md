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

## Commands

<details>
<summary>List All Running Processes</summary>
  
  
List all runing proccesses on client maching and their corresponding pid

**Setup**

'pip install psutil'

'pip install pywin32'


</details>

---

<details>
<summary>upload/download</summary>
upload and download any files between server and client

'upload  LOCATION OF FILE'

'download LOCATION  OF FILE'

Location of file must be exact locaiton, you cannot simply type 'filename.txt' instead you must give the exact path 'C:\users\username\Desktop\filename.txt'

This will be changed soon.

**Setup**

No additional setup required
</details>

---

<details>
<summary>Screenshot</summary>
Take screenshot of client machine and send image back to server
  
**Setup**

'pip install pyautogui'

'pip install Pillow'

pyautogui is used to take screenshot
Pillow is used to read and save image bytes

</details>

---

<details>
<summary>Basic UI Design</summary>

**Setup**

'pip install tkinter'

</details>

---

## Contact
Feel Free to email me with any questions: R2xpdGNo@proton.com

## TODO
- ~~Add List Proccess~~
- ~~Add Image sending client~~
- create version with all commands
- ~~Find UAC Bypass~~
- Implement UAC Bypass into Client side code
- Find user to admin privilege escalation
- Implement user to admin privilege escalation
- Allow for Server to control multiple Clients
- ~~add download/upload to move files between server and client~~
- mkdir / rmdir
- show system info
- shutdown/restart
- execute
- keep track of users current directory to allow for easy upload, download, mkdir, rmdir, and execute
- try using a different method of seperating arguments from commands
- Add User Interface

## Disclaimer
These tools are provided for educational and research purposes only. The author of this project is in no way responsible for any misuse of these tools.
