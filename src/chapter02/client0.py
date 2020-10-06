import socket

HOST = "localhost"
PORT = 50000
BUFF_SIZE = 4096

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server
    client.connect((HOST, PORT))

    # receive message from server
    data = client.recv(BUFF_SIZE)
    print(data.decode("UTF-8"))

finally:
    # close connection
    client.close()
