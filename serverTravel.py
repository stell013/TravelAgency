from socket import *
from helperMudule import *
import pickle

createDict('routes.txt')
#reverseTrip()
#listAllFlights()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = reverseTrip(sentence)
	data= pickle.dumps(capitalizedSentence)

	connectionSocket.send(data.encode())
	connectionSocket.close()