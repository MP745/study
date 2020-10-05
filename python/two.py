from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

msg = clientSock.recv(1024)
print(msg.decode('utf-8'))

msg = '안녕'
clientSock.send(msg.encode('utf-8'))