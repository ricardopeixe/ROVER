from socket import socket, AF_INET, SOCK_STREAM,SOL_SOCKET, SO_REUSEADDR
import re 
from funcao_pedido import *


# Define socket host and port
SERVER_HOST = ''
SERVER_PORT = 80

# Create socket
s = socket(AF_INET, SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(3)

while True:
    # Wait for client connections
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    content = handle_request(request)

    # enviar resposta HTTP
    if content:
        if str(content).find("html") > 0:
            conn.send('HTTP/1.1 200 OK\n\n'.encode())
            conn.sendall(content)
        else:
            conn.send('HTTP/1.1 200 OK\r\n'.encode())
            conn.send("Content-Type: image/jpeg\r\n".encode())
            conn.send("Accept-Ranges: bytes\r\n\r\n".encode())
            conn.sendall(content)

    conn.close()
s.close() # to close the main socket, the loop must be broken