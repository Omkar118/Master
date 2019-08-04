import socket
from threading import Thread
import pickle
import ftplib
import tkinter

TCP_IP = ''
TCP_PORT = 9003
BUFFER_SIZE = 1024

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
                print('data=%s', (data))
                if not data:
                    f.close()
                    print ('file close()')
                    break
                # write data to a file
                f.write(data)
        print('Successfully get the file')
        #s.close()
        self.sock.close()
        print('connection closed')

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

def getFile(conn):

    data = conn.recv(4096)
    directory = pickle.loads(data)

    #Open ftp connection
    ftp = ftplib.FTP(directory[2])
    ftp.login(directory[0], directory[1])

    #List the files in the current directory
    print("File List:")
    files = ftp.dir()
    print(files)

    #Get the readme file
    filename = 'pack.tar.gz'
    ftp.cwd("/home/rushikesh/")
    gFile = open(filename, "wb")
    ftp.retrbinary('RETR '+ filename, gFile.write)
    gFile.close()
    ftp.quit()


while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()

    #retrieve file
    getFile(conn)

    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)
    for t in threads:
       t.join()
