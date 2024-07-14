import socket

HOST = '192.168.56.1'
PORT = 50000

server = (HOST, PORT)

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    lista = ['arquivo_teste.docx', 'batman.txt']
    print(lista)
    arquivo = input("Digite o nome do arquivo que está no servidor: ")
    udpSocket.sendto(arquivo.encode(), server)
    data, endereco = udpSocket.recvfrom(1024)
    print(f"Conteúdo do arquivo '{arquivo}': {data.decode()}")
    with open(arquivo, 'w') as f:
        f.write(data.decode())
