import socket

while True:
    msgFromClient = input("what message do you want to send to the server: ")

    bytesToSend = str.encode(msgFromClient)

    serverAddressPort = ("127.0.0.1", 10805)

    bufferSize  = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

