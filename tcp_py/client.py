import socket


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))

while True:
    print('\nEnter the string: ')
    mystr = input()
    client_sock.send(mystr.encode())
    changed_str = client_sock.recv(1024)
    print('New string: ', changed_str.decode())
client_sock.close()