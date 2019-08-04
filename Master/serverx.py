import socket
from threading import Thread
import ftplib


TCP_IP = ''
TCP_PORT = 9002
BUFFER_SIZE = 5000

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        with open('received_file', 'wb') as f:
            print('file opened')
            while True:
                #print('receiving data...')
                data = conn.recv(BUFFER_SIZE)
                #print('data=%s', (data))
                if not data:
                    f.close()
                    print ('file close()')
                    break
                # write data to a file
                f.write(data)
        print('Successfully get the file')

        self.sock.close()
        print('connection closed')




while True:

    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    for t in threads:
     t.join()




