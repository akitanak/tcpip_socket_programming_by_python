import socket
import select
import datetime

PORT = 50000
BUF_SIZE = 4096

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
        clientno_dict = {}
        clientno = 0
        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)

            for s in readable:
                if s.fileno() == sock.fileno():
                    client, addr = s.accept()
                    inputs.append(client)
                    clientno += 1
                    msg = str(datetime.datetime.now())
                    msgs[client] = msg
                    clientno_dict[client] = clientno
                    print(f"{msg} receive connection request.(client no: {clientno})")
                    print(client)
                else:
                    data = s.recv(BUF_SIZE)
                    if data:
                        c_no = clientno_dict.get(s)
                        print(f"({c_no}) {data.decode('UTF-8')}")
                        msg = msgs.get(s)
                        if msg is not None:
                            s.sendall(msg.encode("UTF-8"))
                        else:
                            s.sendall("NOT FOUND.".encode("UTF-8"))
                    else:
                        inputs.remove(s)
                        msgs.pop(s)
                        print(f"close {s}")
                        s.close()

    except Exception as e:
        print(f"unexpected error occurred. {e}")
