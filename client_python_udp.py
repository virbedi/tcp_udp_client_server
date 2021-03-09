from socket import *

serverName = input('Enter server name or IP address: ')
serverPort = int(input('Enter port: '))

# Port validation 
while serverPort < 0 or serverPort > 65535:
    print('Invalid port number.')
    serverPort = int(input('Enter port: '))

clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get input here 
input = input('Enter command: ')
input = input.encode()
lenght = str(len(input)).encode()

# Send length and input message 
ACK = ''
retry = 0 

while ACK != 'ACK' and retry < 3:
    try:
        clientSocket.sendto(lenght, (serverName, serverPort))
        clientSocket.sendto(input, (serverName, serverPort))
        clientSocket.settimeout(1)
        ACK, addr = clientSocket.recvfrom(2048)
        ACK = ACK.decode()
        clientSocket.settimeout(None)
    except timeout:
        retry += 1

if ACK != 'ACK':
    print('Failed to send command. Terminating.')
    exit()

# Getting server response 
length, addr = clientSocket.recvfrom(1024)
data, addr = clientSocket.recvfrom(2048)
length = int(length.decode())
data = data.decode()

if len(data) == length:
    ACK = 'ACK'
    ACK = ACK.encode()
    clientSocket.sendto(ACK, addr)
 
else:
    print('File transmission failed.')
    exit()

file = open("UDPclientOutput.txt", 'w')
file.write(data)

print()
print('File UDPclientOutput.txt saved.')

exit()

# How to use UDP for python 
# https://wiki.python.org/moin/UdpCommunication
