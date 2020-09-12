import socket

while True:
    try:
        hostname = input("enter hostname.(q: exit)")
        if hostname == "q":
           break
        print(socket.gethostbyname(hostname))
    except:
        print("cannot translate.")

