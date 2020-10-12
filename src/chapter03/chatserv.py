import socket

PORT = 50000
BUFF_SIZE = 4096


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("", PORT))

clist = []
while True:
    data, client = server.recvfrom(BUFF_SIZE)
    if not (client in clist):
        clist.append(client)
    if data.decode("utf-8") == 'q':
        clist.remove(client)
    else:
        msg = f"{str(client)}> {data.decode('utf-8')}"
        print(msg)
        for c in clist:
            server.sendto(msg.encode("utf-8"), c)
