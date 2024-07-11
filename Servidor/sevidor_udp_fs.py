#gravar resposta, espe

import socket, datetime

HOST = ''
PORT = 50000
clientDir = {}

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))
print('Server on-line...')
