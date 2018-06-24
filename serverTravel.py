from socket import *
from helperMudule import *
import pickle

createDict('routes.txt')
reverseTrip()


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	#capitalizedSentence = listAllFlights(sentence)
	#capitalizedSentence = travelFrom(sentence)
	capitalizedSentence = travelTo(sentence)
	data = pickle.dumps(capitalizedSentence)

	connectionSocket.send(data.encode())
	connectionSocket.close()


#have a single method that receives the commands and on the HELPERMODULE
#CALL EACH METHOD FOR EACH COMMAND