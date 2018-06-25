from socket import *
from helperMudule import *
#import pickle
import json

createDict('routes.txt')
reverseTrip()


serverPort = 10000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept()
	print("Connected with " + addr[0] + ":" + str(addr[1]))
	
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = commandHandler(sentence)
	data = json.dumps(capitalizedSentence)

	connectionSocket.send(data.encode())
	connectionSocket.close()

serverSocket.close()