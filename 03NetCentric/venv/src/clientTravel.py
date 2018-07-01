from socket import *

#import pickle
import json
import struct


serverName = 'localhost'
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
	
while True:
	sentence = input('\nTell us what do you need : \n')
	clientSocket.send(sentence.encode())

	if sentence.upper() == 'QUIT':
		clientSocket.close()
		break

	modifiedSentence = clientSocket.recv(1024)
	decodeSent = modifiedSentence.decode()
	myData = json.loads(decodeSent)

	for up in myData:
  		 print(up)


	#clientSocket.close()
