import socket
import sys

HOST = '192.168.56.1'
PORT = 50000

server = (HOST, PORT)
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
 lista = ['arquivo_teste.docx', 'batman.txt', 'superman.txt']
 print('Os arquivos disponíveis no servidor:', lista)
 arquivo = input("Digite o nome do arquivo que está no servidor ou 0 para sair do programa: ")
 
 if arquivo == '0':
    print('Saindo do programa...')
    udpSocket.sendto(arquivo.encode(), server)
    sys.exit()
    
 udpSocket.sendto(arquivo.encode(), server)
 data, endereco = udpSocket.recvfrom(1024)
 print(f"Conteúdo do arquivo '{arquivo}': {data.decode()}")
 with open(arquivo, 'w') as f:
        f.write(data.decode())
