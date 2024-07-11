import socket

HOST = '192.168.2.245'
PORT = 50000

server = (HOST, PORT)

ARQ


udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    arquivo=input("Digita o nome do arquvio que tem no servidor")
    
    udpSocket.sendto(arquivo, server)
