from socket import *

serverName = input('Enter server name or IP address: ')
serverPort = int(input('Enter port: '))

# Port validation 
if serverPort < 0 or serverPort > 65535:
    print('Invalid port number.')
    exit()

# Try connecting to server
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverName, serverPort))
except OSError:
    print('Could not connect to server.')
    exit()

# Send client input to server 
clientInput = input('Enter command: ')
clientSocket.send(clientInput.encode())

# Write Server response to file
response = clientSocket.recv(2048).decode()
file = open("TCPclientOutput.txt", 'w')
file.write(response)

print('File TCPclientOutput.txt saved.')

clientSocket.close()