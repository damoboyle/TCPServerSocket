from socket import *
from select import *
from threading import Thread
import tkinter

BUFFSIZE = 1024

serverName = 'localhost'
serverPort = 5050

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) 
clientSocket.send(bytes(input('Enter Username: '), 'utf8'))

def receive():
    while True:
        try:
            msg = clientSocket.recv(BUFFSIZE).decode()
            msgList.insert(tkinter.END, msg)
        except OSError:
            break

def send(event = None):  # event passed by binders
    msg = message.get()
    message.set('')
    clientSocket.send(msg.encode())
    
    if msg == '{quit}':
        clientSocket.send(msg.encode())
        clientSocket.close()
        app.destroy()

def close(event = None):
    message.set('{quit}')
    send()

app = tkinter.Tk()
app.title('ClassChat')

messageFrame = tkinter.Frame(app)
scrollbar = tkinter.Scrollbar(messageFrame)
msgList = tkinter.Listbox(messageFrame, height = 25, width = 60, xscrollcommand = scrollbar.set, bg = 'black', fg = 'white')

messageFrame.pack()
scrollbar.pack(side = tkinter.RIGHT, fill = tkinter.Y)
msgList.pack(side = tkinter.LEFT, fill = tkinter.BOTH)

#InputBar
message = tkinter.StringVar()#Needed for sending messages
entry = tkinter.Entry(app, textvariable = message, width = 50, bg = 'white')
entry.bind('<Return>', send)
entry.pack(padx = 5, side = tkinter.LEFT)

#Send Button
button = tkinter.Button(app, text = 'Send', command = send, width = 10, bg = 'blue', fg = 'white')
button.pack(padx = 5, pady = 10)

app.protocol('WM_DELETE_WINDOW', close)

receiveThread = Thread(target = receive)
receiveThread.start()

#Starts GUI
tkinter.mainloop()
