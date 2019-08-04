import socket



TCP_IP = '192.168.0.27'
TCP_PORT = 9001
BUFFER_SIZE = 5000
flag = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename='rf'
f = open(filename,'rb')
while True:
    l = f.read(BUFFER_SIZE)
    while (l):
        s.send(l)
        #print('Sent ',repr(l))
        l = f.read(BUFFER_SIZE)
        if not l:
          flag = 1
          f.close()
          s.close()
          break

        if flag == 1:
            break
