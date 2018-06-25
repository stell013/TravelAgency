from socket import *
serverName = 'localhost'
#import pickle
import json

"""def startConn():
	serverPort = 10000
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	print("Welcome to the TravelAgency")"""

while True:
	serverPort = 10000
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	

	sentence = input('\nTell us what do you need : \n')
	clientSocket.send(sentence.encode())

	modifiedSentence = clientSocket.recv(1024)
	decodeSent = modifiedSentence.decode()
	myData = json.loads(decodeSent)

	for up in myData:
  		 print(up)


	clientSocket.close()
