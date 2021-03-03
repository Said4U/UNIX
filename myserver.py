#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
print('Server start')
sock.bind(('', 9090))
print('Server listening...')
sock.listen(1)
conn, addr = sock.accept()

print('Connected:', addr)
print('Receiving data')
passage = True

while True:
    data = conn.recv(1024)
    if not data:
        print('Connection close')
        break
    if passage:
        print('Sending data')
        passage = False
    conn.send(data)

conn.close()
print('Server close')


