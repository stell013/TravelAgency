from socket import *
from helperModule import *
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
serverSocket.listen(10)
print('The server is ready to receive')



def clientT(conn):
	

	while True:
	
		sentence = conn.recv(1024).decode()
		if not sentence:
			break;
		response = commandHandler(sentence,conn)
		data = json.dumps(response)
		conn.send(data.encode())


	conn.close()





while 1:
	connectionSocket, addr = serverSocket.accept()
	print("Connected with " + addr[0] + ":" + str(addr[1]))
	start_new_thread(clientT, (connectionSocket,) )


serverSocket.close()

