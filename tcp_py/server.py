# -*- coding: utf-8 -*-
import socket


def change(tmp):                        # Заменяет каждый 4-ый элемент на %
    i = -1
    while i != len(tmp):
        if i % 4 == 0 and i != 0:
            tmp = tmp[:i - 1] + '%' + tmp[i:]
        i += 1
    return tmp


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)    # создаём сокет сервера
server_sock.bind(('127.0.0.1', 53210))                                      # связываем сокет с хостом и портом
server_sock.listen(1)                                                       # режим прослушивания
print('\nServer is active\n')
while True:
    client_sock, client_addr = server_sock.accept()                         # получаем сокет клиента и его адрес
    print('Connected by ', client_addr)

    while True:
        str_to_change = client_sock.recv(1024)
        if not str_to_change:
            break
        print('String received: ', str_to_change)
        newstr = change(str_to_change.decode())
        client_sock.send(newstr.encode())
        print('New string', '"', newstr.encode(), '"', 'has been sent\n')

    client_sock.close()
    print('socket closed\n')
