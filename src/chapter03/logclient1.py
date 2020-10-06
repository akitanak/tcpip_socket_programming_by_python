import socket
import sys

HOST = "localhost"
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except Exception as ex:
    print(f"cannot connect server. {ex}")
    sys.exit(-1)

while True:
    msg = input()
    if msg == "q":
        break
    client.sendall(msg.encode("UTF-8"))

client.close()
