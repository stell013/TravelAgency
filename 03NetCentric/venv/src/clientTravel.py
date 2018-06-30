from socket import *
serverName = 'localhost'
#import pickle
import json
import struct



serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
	
while True:
	sentence = input('\nTell us what do you need : \n')
	clientSocket.send(sentence.encode())

	if sentence.upper() == 'QUIT':
		clientSocket.close()

	modifiedSentence = clientSocket.recv(1024)
	decodeSent = modifiedSentence.decode()
	myData = json.loads(decodeSent)

	for up in myData:
  		 print(up)


	#clientSocket.close()
