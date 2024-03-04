from socket import *
import threading
import random

def handle_client(connectionSocket, addr):
    print(addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode().strip()
        print(sentence)
        response = "Didn't understand, please send a proper message"
        if sentence == "exit":
            keep_communicating = False
            response = "closing the connection"
            connectionSocket.send(response.encode())
        elif sentence.startswith("random"):
            response = "Input 2 numbers and I will return a random number between the two"
            connectionSocket.send(response.encode())
            input_numbers = connectionSocket.recv(1024).decode().strip()
            tal1, tal2 = map(int, input_numbers.split())
            response = "Heres your random number: " + str(random.randint(tal1, tal2))
            connectionSocket.send(response.encode())

        elif sentence.startswith("add"):
            response = "Input 2 numbers and I will return the sum of them"
            connectionSocket.send(response.encode())
            input_numbers = connectionSocket.recv(1024).decode().strip()
            tal1, tal2 = map(int, input_numbers.split())
            response = "Here is the sum of your selected numbers: " + str(tal1 + tal2)
            connectionSocket.send(response.encode())
        elif sentence.startswith("subtract"):
            response = "Input numbers and I will subtract the second from the first"
            connectionSocket.send(response.encode())
            input_numbers = connectionSocket.recv(1024).decode().strip()
            tal1, tal2 = map(int, input_numbers.split())
            response = "Here is the value of the subtracted numbers: " + str(tal1 - tal2)
            connectionSocket.send(response.encode())          
    connectionSocket.close()
    print("Connection closed")
            

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()