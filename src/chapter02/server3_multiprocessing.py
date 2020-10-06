import socket
import datetime
import multiprocessing as mp

PORT = 50000
BUF_SIZE = 4096


def client_handler(client, clientno, msg):
    try:
        data = client.recv(BUF_SIZE)
        print(f"({clientno}) {data.decode('UTF-8')}")
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

    clientno = 0
    mp.set_start_method("fork")
    while True:
        client, addr = server.accept()
        clientno += 1
        msg = str(datetime.datetime.now())
        print(f"{msg} receive connection request.(client no: {clientno})")
        print(client)

        p = mp.Process(
            target=client_handler, args=(client, clientno, msg)
        )
        p.start()

except Exception as e:
    print(f"unexpected error occurred. {e}")

finally:
    if client:
        client.close()

    server.close()
