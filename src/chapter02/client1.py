import socket
import sys

PORT = 50000
BUFF_SIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("target server: ")

try:
    # connect to server.
    client.connect((host, PORT))

    # send message to server.
    msg = input("input your message: ")
    client.sendall(msg.encode("UTF-8"))

    # receive message from server.
    data = client.recv(BUFF_SIZE)
    print(f"message from server: {data.decode('UTF-8')}")

except Exception as e:
    print(f"cannot connect server.\n{e}")
    sys.exit(1)

finally:
    client.close()
