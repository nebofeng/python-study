import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8000))
while True:
    sock.send(input(">>>").encode())
sock.close()
