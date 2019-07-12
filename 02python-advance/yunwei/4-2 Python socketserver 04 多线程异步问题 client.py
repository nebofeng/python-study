#coding:utf-8
import json
import time
import socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8005))
sock.send("hello I am client1")
file_header = json.loads(sock.recv(1024))
request_header = {
    "method": "get",
    "name": file_header["name"]
}
sock.send(json.dumps(request_header))
if request_header[u"method"] == u"get":
    f = open(request_header[u"name"],"a")
#假使我们每次只接受512
file_size = file_header[u"size"]
down_num = file_size/512
if int(down_num) == down_num:
    pass
else:
    down_num = int(down_num)+1
for i in range(down_num):
    data = sock.recv(512)
    print(data)
    f.write(data)
f.close()
sock.close()
