from socket import *
serverName = 'localhost'
import pickle

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Return a numer of seats: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
decodeSent = modifiedSentence.decode()
myData = pickle.loads(decodeSent)
for up in myData:
  print(up)
clientSocket.close()