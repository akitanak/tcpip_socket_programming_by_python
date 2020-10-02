import socket
import select
import datetime

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
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        # set non-blocking
        sock.setblocking(0)
        sock.bind(("", PORT))
        sock.listen()

        inputs = [sock]
        outputs = []
        msgs = {}
        clientno = 0
        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s is sock:
                    client, addr = s.accept()
                    inputs.append(client)
                    clientno += 1
                    msg = str(datetime.datetime.now())
                    msgs[client] = msg
                    print(f"{msg} receive connection request.(client no: {clientno})")
                    print(client)
                else:
                    data = s.recv(BUF_SIZE)
                    if data:
                        print(f"({clientno}) {data.decode('UTF-8')}")
                        msg = msgs.get(s)
                        if msg is not None:
                            client.sendall(msg.encode("UTF-8"))
                        else:
                            client.sendall("NOT FOUND.".encode("UTF-8"))
                    else:
                        inputs.remove(s)
                        msgs.pop(s)
                        print(f"close {s}")
                        s.close()

    except Exception as e:
        print(f"unexpected error occurred. {e}")