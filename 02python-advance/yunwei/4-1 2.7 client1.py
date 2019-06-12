import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8000))
while True:
    sock.send(input(">>>").encode())
#    sock.send("hello world I am 01".encode())

sock.close()
