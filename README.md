# tcp_udp_client_server
Basic utilization of TCP and UDP Client Server Interaction.

 The general interaction between the client and server is as follows:

    The server starts and waits for a connection to be established by the client.
    When a command is received, then the server will:
        Issue the command to its system and store the output in a file.
        Open the file, read its content to a buffer.
        Write the buffer contents to the connection established by the client. 
    The client will receive the data from the socket and store it in a local file.