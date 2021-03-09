# tcp_udp_client_server
Basic utilization of TCP and UDP Client Server Interaction.
  
TCP is a connection-oriented protocol. Connection-orientation means that the communicating devices should establish a connection before transmitting data and should close the connection after transmitting the data.

UDP is the Datagram oriented protocol. This is because there is no overhead for opening a connection, maintaining a connection, and terminating a connection. UDP is efficient for broadcast and multicast type of network transmission.

In order to have reliable UDP transmission, I have implemented ACK messages and retransmission in case of lost packets. 

 The general interaction between the client and server is as follows:

    The server starts and waits for a connection to be established by the client.
    When a command is received, the server will:
        Issue the command to its system and store the output in a file.
        Open the file, read its content to a buffer.
        Write the buffer contents to the connection established by the client. 
    The client will receive the data from the socket and store it in a local file.
