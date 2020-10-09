from socket import *
import threading
import time

lock = threading.Lock()

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8')) # connectionSock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024).decode('utf-8')
        print(connectlist.index(sock),' :', recvData)
        for i in range(len(connectlist)):
            if connectlist[i] == sock:
                pass
            else:
                connectlist[i].send((str(connectlist.index(sock)) + " : " + recvData).encode('utf-8'))

def name(sock):
    for i in range(len(connectlist)):
        if connectlist[i] == sock:
            connectlist[i].send(('당신은' + str(connectlist.index(sock)) + ' 번 입니다.').encode('utf-8'))
            

def connect():
    while True:
        connectionSock, addr = serverSock.accept()
        connectlist.append(connectionSock)
        print(str(addr), '에서 접속되었습니다.')
        receiver = threading.Thread(target=receive, args=(connectionSock,))
        receiver.start()
        namer = threading.Thread(target=name, args=(connectionSock,))
        namer.start()

connectlist=[]

port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen()

print("%d번 포트로 접속 대기중..."%port)

connector = threading.Thread(target=connect, args=())

connector.start()

while True:
    lock.acquire()
    time.sleep(1)
    lock.release()
    pass
