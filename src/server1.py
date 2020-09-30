import socket
import datetime

PORT = 50000


def send_message(client):
    try:
        msg = str(datetime.datetime.now())
        client.sendall(msg.encode("UTF-8"))
        print("receive connection request.")
        print(client)
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
