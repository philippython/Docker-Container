import socket

localIP = "127.0.0.1"

localPort = 10805

bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

messages = 0
# Listen for incoming datagrams
while(True):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    if message:
        # adding up new messages
        messages += 1
    
    def number_filterer(char):
        try:
            int(char)
        except ValueError:
            pass
        else:
            return int(char)
        
    print(f"Server has received {messages} messages.")
    decoded_msg = str(bytes.decode(message, 'utf-8'))
    clientMsg = "Message from Client: {}".format(decoded_msg)
    filtered_numbers = filter(number_filterer, decoded_msg)
    
    # list of all numbers in the client message
    numbers = list(filtered_numbers)
    

    print(f"The Client message is {len(decoded_msg)} long.")
    print(f"Client message contains {len(numbers) + decoded_msg.count('0')} numbers")
    print(clientMsg)
   