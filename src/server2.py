import socket
import datetime

PORT = 50000
BUF_SIZE = 4096


def send_message(client):
    try:
        msg = str(datetime.datetime.now())
        print("receive connection request.")
        print(client)

        data = client.recv(BUF_SIZE)
        print(data.decode("UTF-8"))

        client.sendall(msg.encode("UTF-8"))
    except Exception as e:
        print(f"unexpected errror.{e}")
    finally:
        client.close()


client = None
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(("", PORT))
    server.listen()

    while True:
        client, addr = server.accept()
        send_message(client)


except Exception as e:
    print(f"unexpected error occurred. {e}")

finally:
    if not client:
        client.close()

    server.close()
