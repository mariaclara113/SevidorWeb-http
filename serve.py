# server.py
from socket import *
import sys

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
serverPort = 6789               
serverSocket.bind(('', serverPort))
serverSocket.listen(1)          

print(f"Servidor HTTP simples rodando na porta {serverPort}...")

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        message = connectionSocket.recv(1024).decode()
        print("---- Requisição recebida ----")
        print(message)
 

        filename = message.split()[1]
        f = open(filename[1:])                
        outputdata = f.read()
        f.close()

        # Envia a linha de status do cabeçalho HTTP
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send(f"Content-Length: {len(outputdata.encode())}\r\n".encode())

        # linha em branco separando cabeçalho do corpo
        connectionSocket.send("\r\n".encode())

        # Envia o conteúdo do arquivo ao cliente
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        error_body = "<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send(f"Content-Length: {len(error_body.encode())}\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send(error_body.encode())

        # Fecha o socket do cliente
        connectionSocket.close()

# (Nunca alcançado em execução normal do loop infinito)
    serverSocket.close()
    sys.exit()
