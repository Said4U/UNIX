#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print('8.Connected')

text = input("Введите ваш текст: \n")
print('\n10.Sending data')
sock.send(text.encode())

print('11.Receiving data')
data = sock.recv(1024)

sock.close()
print('9.Unconnected\n')

print('Ответ от сервера:')
print(data.decode())



