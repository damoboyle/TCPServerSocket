from socket import *
from threading import *
import time

BUFFSIZE = 1024

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 5050))

history = []
sender = []
clientList = []
addresses = []

def handleClient(conn, addr): 
    username = conn.recv(BUFFSIZE).decode().lower()
    addresses.append(conn)
    clientList.append(username)

    #Handles immediate client quit
    if username != '{quit}':
        conn.send(bytes(f'Welcome [{username}]', 'utf8'))
        time.sleep(1)
        conn.send(bytes('You have Successfully Connected to ClassChat Server', 'utf8'))          
        new = f'New Connection: [{username}]'
        print(new, addr)#Server Record
        broadcast(new, 'server')
        
    else:
        conn.close()
        addresses.remove(conn)
        clientList.remove(username)

    #BONUS#
    #Receive Missed Messages
    for missed in history:
        if username == missed.partition(':')[0]:
            missedMSG = f"[server] You Missed:[{sender[history.index(missed)]}] {missed.rpartition(':')[0]}"
            conn.send(missedMSG.encode())
            
        elif missed.partition(':')[0] == 'all':
            missedToAll = f"[server] You Missed:[{sender[history.index(missed)]}] ToAll: {missed.rpartition(':')[0]}"
            conn.send(missedToAll.encode())
    
    while True:
        try:
            message = conn.recv(BUFFSIZE).decode()

            if message != '{quit}':
                history.append(message)
                sender.append(username)
                
                chat = message.partition(':')
                if chat[1] != ':':
                    conn.send(bytes('Message not sent, No recipirent!', 'utf8'))
                    time.sleep(1)
                    conn.send(bytes('(Format) username:message ', 'utf8'))
                elif chat[0].lower() == 'all':
                    broadcast(chat[2], username)
                else:
                    send(chat[0], chat[2], username, conn)
                    conn.send(message.encode())

                print (f'[{username}]', message)

            #Logs user out of the server    
            else:
                addresses.remove(conn)
                clientList.remove(username)
        except:
            conn.close()

def send(to, msg, you, fail):
    private = f'[{you}] {msg}'
    
    for user in clientList:
        if user == to:
            addresses[clientList.index(to)].send(private.encode())
            break
    else:
        fail.send(bytes('!!Headsup!!', 'utf8'))
        time.sleep(1)
        fail.send(bytes(f'User:{to} is not online right now', 'utf8'))
        time.sleep(1)
        fail.send(bytes('We will send them this message when they come online', 'utf8'))

#BONUS#
#Group Chat
def broadcast(msg, you):
    group = f'[{you}] ToAll: {msg}'
    
    for client in addresses:
        client.send(group.encode())
            
def start():
    serverSocket.listen()
    print ('Server is online!')
    
    while True:
        clientSocket, addr = serverSocket.accept()
        thread = Thread(target = handleClient, args = (clientSocket, addr))
        thread.start()

print ('Starting Server...')
start()
