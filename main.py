from _thread import *

import socket
import random
import sympy
import os

def multi_threaded_client(connection, number):
    connection.send(str.encode(i))
    connection.send(str.encode(p))

    data = connection.recv(1024)
    data = data.decode('utf-8')
    sign = connection.recv(1024)

    client_data[number] = {'data': data,
                            'sign': sign}

    while True:
        if len(client_data) == 2:
            if number == 1:
                connection.sendall(str.encode(str(client_data[0]['data'])))
                connection.sendall(client_data[0]['sign'])
                break
            else:
                connection.sendall(str.encode(str(client_data[1]['data'])))
                connection.sendall(client_data[1]['sign'])
                break

    connection.close()

if __name__ == "__main__":
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    ThreadCount = 0
    client_data = {}
    
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening...')
    ServerSideSocket.listen(2)

    i = str(random.randrange(1649, 4561))
    p = str(sympy.randprime(400, 1000))

    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client, ThreadCount))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

    ServerSideSocket.close()