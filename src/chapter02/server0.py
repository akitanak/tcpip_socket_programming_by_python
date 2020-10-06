import socket

PORT = 50000

client = None
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(("", PORT))
    server.listen()

    client, addr = server.accept()
    client.sendall(b"Hi! nice to meet you!\n")

except Exception as e:
    print(f"unexpected error occurred. {e}")

finally:
    if not client:
        client.close()

    server.close()
