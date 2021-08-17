#!/usr/bin/env python3

import webbrowser

import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexao de um cliente de conexao')
conn, ender = s.accept()

print('Conectado em', ender)
while True:
    data = conn.recv(1024)
    if not data:
        webbrowser.open('https://www.youtube.com')
        conn.close()
        break
    conn.sendall(data)

