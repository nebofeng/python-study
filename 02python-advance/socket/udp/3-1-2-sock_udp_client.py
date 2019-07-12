#coding:gbk
import socket
"""
print("this is server ? 8010")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",8010))
while True:
    send_data = raw_input(">>>")
    sock.sendto(send_data,("127.0.0.1",8009))
    if send_data == "break":
        break
    con,add = sock.recvfrom(512)
    print("%s:%s is connected"%add)
    print(con)
    if con == "break":
        break
    
sock.close()
"""
print("this is server ? 8010")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",8010))
while True:
    send_data = raw_input(">>>")
    sock.sendto(send_data,("127.0.0.1",8009))
    if send_data == "break":
        break
    #con,add = sock.recvfrom(512)
    #print("%s:%s is connected"%add)
    #print(con)
    #if con == "break":
    #    break
sock.close()











