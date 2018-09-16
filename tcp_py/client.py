import socket


print('\nEnter the string: ')
mystr = input()

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Создаём скоет клиента
client_sock.connect(('127.0.0.1', 53210))                           # Подключаемся к серверу
client_sock.send(mystr.encode())                                    # Отправляем строку
changed_str = client_sock.recv(1024)                                # Получаем изменённую строку
client_sock.close()                                                 # Закрываем сокет
print('The new string is: ', changed_str.decode())