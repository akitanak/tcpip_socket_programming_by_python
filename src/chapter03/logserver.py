import socket
import datetime

PORT = 50000
BUFF_SIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen()

while True:
    client, addr = server.accept()
    d = datetime.datetime.now()
    fname = d.strftime("%m%d%H%M%S%f")
    print(fname, "I got a connection request.")
    print(client)
    with open(fname + ".txt", "wt") as fout:
        try:
            while True:
                data = client.recv(BUFF_SIZE)
                if not data:
                    break

                print(data.decode("UTF-8"))
                print(data.decode("UTF-8"), file=fout)
        except Exception as ex:
            print(f"Error was occurred.(disconnect) {ex}")

    client.close()
