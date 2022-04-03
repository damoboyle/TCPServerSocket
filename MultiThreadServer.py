from socket import *
from threading import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 5050))

def handleClient(conn, addr):
    print('New Connection:', addr)
    success = 'Successfully Connected to ClassChat Server'
    conn.send(success.encode())
    
    while True:
        message = conn.recv(1024).decode()

        if message:    
            print (addr, ': ', message)
            conn.send(message.encode())        
        else:
            conn.close()

def start():
    serverSocket.listen()
    print ('Server is online!')
    
    while True:
        clientSocket, addr = serverSocket.accept()
        thread = Thread(target = handleClient, args = (clientSocket, addr))
        thread.start()

print ('Starting Server...')
start()

