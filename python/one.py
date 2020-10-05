from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

msg = '안녕'
connectionSock.send(msg.encode('utf-8'))

msg = connectionSock.recv(1024)
print(msg.decode('utf-8'))