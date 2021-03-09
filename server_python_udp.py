from socket import *
import subprocess

serverName = '127.0.0.1'

try:
    serverPort = 8655 #int(input())
except error:
    print('Invalid port number.')
    exit()

# Port validation 
while serverPort < 0 or serverPort > 65535:
    print('Invalid port number.')
    exit()

serverSocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind((serverName, serverPort))

while True:
    # Getting client command 
    length, addr = serverSocket.recvfrom(1024)
    data, addr = serverSocket.recvfrom(2048)

    length = int(length.decode())
    data = data.decode()
    
    if len(data) == length:
        ACK = 'ACK'
        ACK = ACK.encode()
        serverSocket.sendto(ACK, addr)
    
    else:
        print('Failed to receive instructions from the client.')
        
    # Run command and get server output from file 
    output = subprocess.run([data], stdout=subprocess.PIPE).stdout.decode('utf-8') 
    file = open("UDPserverOutput.txt", 'w')
    file.write(output)

    # Send contents of output file to Client 
    file = open("UDPserverOutput.txt", 'r')
    
    serverResponse = file.read().encode()
    length = str(len(serverResponse)).encode()

    serverSocket.sendto(length, addr)
    serverSocket.sendto(serverResponse, addr)

    retry = 0
    ACK = ''
    
    while ACK != 'ACK' and retry < 3:
        ACK, addr = serverSocket.recvfrom(1024)
        ACK = ACK.decode()

    if ACK != 'ACK':
        print('File transmission failed')

# How to use UDP for python 
# https://wiki.python.org/moin/UdpCommunication
