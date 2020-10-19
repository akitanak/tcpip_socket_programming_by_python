import socket
import threading
from queue import Queue

PORT = 50000
BUFF_SIZE = 4096


def msg_receiver(client, queue):
    try:
        while True:
            data = client.recv(BUFF_SIZE)
            data = data.decode("utf-8")
            if data == "q":
                break
            else:
                msg = f"{str(client)}> {data}"
                print(msg)
                queue.put(msg)
    except Exception as e:
        print(e)
    finally:
        client.close()


def msg_sender(clients, queue):
    try:
        while True:
            msg = queue.get(True)

            for client in clients:
                try:
                    if client.fileno() != -1:
                        client.sendall(msg.encode("utf-8"))
                except Exception as e:
                    print(f"send msg was failed. {e}")
                    clients.remove(client)

    except Exception as e:
        print(e)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen()

clients = []
msg_queue = Queue()
sender_thread = threading.Thread(target=msg_sender, args=(clients, msg_queue))
sender_thread.start()
print("Server was started. waiting for client messages...")

while True:
    client, addr = server.accept()
    clients.append(client)
    receiver_thread = threading.Thread(target=msg_receiver, args=(client, msg_queue))
    receiver_thread.start()
