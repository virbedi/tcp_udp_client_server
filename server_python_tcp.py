from socket import *
import subprocess

serverName = '127.0.0.1'
try:
    serverPort = int(input())
except error:
    print('Invalid port number.')
    exit()

# Port validation 
while serverPort < 0 or serverPort > 65535:
    print('Invalid port number.')
    exit()

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))

serverSocket.listen(1)

while True:
    soc, addr = serverSocket.accept()

    # Receive command from client  
    inputCommand = soc.recv(2048).decode()

    # Collect shell output 
    output = subprocess.run([inputCommand], stdout=subprocess.PIPE).stdout.decode('utf-8')

    # Write contents of shell output to file 
    file = open("TCPserverOutput.txt", 'w')
    file.write(output)

    # Send contents of output file to Client 
    file = open("TCPserverOutput.txt", 'r')
    serverResponse = file.read()
    soc.send(serverResponse.encode())

    soc.close()


    # Executing shell commands and collecting output 
    # https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output