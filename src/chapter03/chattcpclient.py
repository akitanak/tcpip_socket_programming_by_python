import socket
import threading


PORT = 50000
BUFF_SIZE = 4096


def server_handler(client):
    try:
        while True:
            data = client.recv(BUFF_SIZE)
            print(data.decode("utf-8"))
    except Exception as e:
        print(e)

    finally:
        client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    host = input("接続サーバ: ")
    if host == "":
        host = "localhost"

    client.connect((host, PORT))
    receive_thread = threading.Thread(target=server_handler, args=(client,))
    receive_thread.start()

    while True:
        msg = input("")
        if msg == "q":
            break
        client.sendall(msg.encode("utf-8"))

except Exception as e:
    print(e)
finally:
    client.close()
