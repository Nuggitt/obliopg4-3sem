from socket import *

def communicate_with_server(sentence):
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    print('From server: ', modifiedSentence)
    tal1 = input('Indtast tal1: ')
    tal2 = input('Indtast tal2: ')
    combined_tals = tal1 + ' ' + tal2
    clientSocket.send(combined_tals.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    print('From server: ', modifiedSentence)

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

keep_communicating = True

while keep_communicating:
    sentence = input('\nWelcome here is your options \nMenu: Random, Add, Subtract, close: ')
    sentence = sentence.lower()
    if sentence == "close":
        print("closing the connection")
        keep_communicating = False
    elif sentence.strip().startswith("random") or sentence.strip().startswith("add") or sentence.strip().startswith("subtract"):
        communicate_with_server(sentence)
    else:
        print("Invalid input: [" + sentence + "] Please choose one of the options: Random, Add, Subtract, exit " )

clientSocket.close()
