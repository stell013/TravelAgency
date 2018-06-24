from socket import *
serverName = 'localhost'
#import pickle
import json

serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Welcome to the TravelAgency")


sentence = raw_input('Tell us what do you need : ')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
decodeSent = modifiedSentence.decode()
myData = json.loads(decodeSent)

for up in myData:
   print(up)



clientSocket.close()