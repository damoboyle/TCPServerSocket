These programs were written for the python 3.8.2 interpreter

Part 1:
The TCPserver.py and TCPclient.py files are designed to be used in tandem
To make use of this TCP client/server pair:

1) Run TCPserver.py
2) Run TCPclient.py
3) When prompted enter some text into the command line

The client program will send the message to the server through a TCP socket, 
the server will then send the message back to the client

Part 2 and 3:
The AdvancedClient.py and MultiThreadServer.py were designed to be used in tandem
To make use of this TCP client/server pair:

1) Run MultiThreadServer.py
2) Run AdvancedClient.py
3) AdvancedClient.py will prompt for a username in the command interface, enter a name into the command line,
	AdvancedClient.py will then generate a GUI, the GUI will display connection information sent from the server.
4) Enter some text into the input box provided in the GUI and press (Send)
	The client GUI will encode this text data and send it the server application.
	The server application will send the text back to the client, and the client will display this in its output.
5) Complete steps 2, 3 and 4 again, with the original GUI still active to make use of the multi-threaded functionality.
6) The GUI can be exited either by entering {quit} in the input field and pressing (Send) or by pressing the window close button.

Part 4 and 5:
The AdvancedClient.py and server.py were designed to be used in tandem
To make use of this TCP client/server pair:

1) Run server.py
2) Run AdvancedClient.py
3) AdvancedClient.py will prompt for a username in the command interface, enter a name into the command line,
	AdvancedClient.py will then generate a GUI, the GUI will display connection information sent from the server.
4) To send a message to a specific client, you must input a formatted as such; user:message and press (Send)
	Where user is the username of the intended recipient and message is the message you wish to send.
	The client GUI will encode this text data and send it the server application.
	The server application will take this data and match it to the intended recipient
	The server will then send the message to the corresponding client thread.
5) To send a message to the group, you must input a formatted as such; all:message and press (Send)
	Where all is a constant and message is the message you wish to send.
	The client GUI will encode this text data and send it the server application.
	The server application will take this data and broadcast it to each recipient thread current connected.
6) The GUI can be exited either by entering {quit} in the input field and pressing (Send) or by pressing the window close button.

No Makefile has been provided for any of the individual modules created for this project as it was deemed unneccessary.