import socket
import threading
import sys

PORT = 50000
BUFF_SIZE = 4096


def server_handler(client):
    try:
        while True:
            data = client.recv(BUFF_SIZE)
            print(data.decode("utf-8"))
    except Exception as e:
        print(e)
        sys.exit(-1)

    finally:
        client.close()


try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = input("接続サーバ: ")
    if host == "":
        host = "localhost"

    p = threading.Thread(target=server_handler, args=(client,))
    p.setDaemon(True)

    while True:
        msg = input("")
        client.sendto(msg.encode("utf-8"), (host, PORT))
        if msg == "q":
            break

        if not p.is_alive():
            p.start()

finally:
    client.close()
