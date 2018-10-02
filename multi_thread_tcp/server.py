import socket
import _thread


trip1 = ["001", "bus", "90 rub", "Mogilev"]
trip2 = ["002", "bus", "70 rub", "Kiev"]
trip3 = ["003", "mini-bus", "13 rub", "Gomel"]
trip4 = ["004", "mini-bus", "10 rub", "Rechitsa"]
trip5 = ["005", "bus", "60 rub", "Smorgon"]
trips_array = [trip1, trip2, trip3, trip4, trip5]


def thread_task(socket, address):
    print("new thread is active")
    while True:
        to_send = ""
        trip_destination = socket.recv(1024)
        if not trip_destination:
            print("client ", address, " disconnected")
            break
        print("destination point received ", trip_destination.decode(), "by ", address)
        for i in range(4):
            if trips_array[i][3] == trip_destination.decode():
                for j in range(4):
                    to_send = to_send + trips_array[i][j] + " "
        if to_send == "":
            to_send = "No matches found"
        socket.send(to_send.encode())


server_address = ('localhost', 9090)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print("//-----------server is active-----------//")
while True:
    client_socket, client_address = server_socket.accept()
    print('Connected by ', client_address)
    _thread.start_new_thread(thread_task, (client_socket, client_address))