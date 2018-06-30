from socket import *
from helperMudule import *
#import pickle
import json
from _thread import *
import sys


createDict('routes.txt')
reverseTrip()
createDictroundedTrip()


serverPort = 10000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print('The server is ready to receive')



def clientT(conn):
	
	#welcome = "Welcome"
	#conn.send(welcome.encode())

	while True:
	
		sentence = conn.recv(1024).decode()
		if not sentence:
			break;
		capitalizedSentence = commandHandler(sentence)
		data = json.dumps(capitalizedSentence)
		conn.send(data.encode())


	conn.close()





while 1:
	connectionSocket, addr = serverSocket.accept()
	print("Connected with " + addr[0] + ":" + str(addr[1]))
	start_new_thread(clientT, (connectionSocket,) )


serverSocket.close()

