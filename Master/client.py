import socket
import ftplib
from tkinter import *
from tkinter import filedialog
import pickle


TCP_IP = '192.168.0.27'
TCP_PORT = 9001
BUFFER_SIZE = 1024

def write():
    #username.set("a default value")
    user = e1.get()

    #password.set("a default value")
    pwd = e2.get()


    if user == "" or pwd == "":
        exit()

    #ftp = ftplib.FTP("localhost")
    #ftp.login(user, pwd)

    #data = []
    #ftp.dir(data.append)
    #ftp.quit()

    #for line in data:
     #   print("-", line)

    #directory = pickle.dumps(data)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    #s.send(directory)

    filename='good.txt'
    f = open(filename,'rb')
    flag = 0
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





master = Tk()

L1 = Label(master, text='User name').grid(row=0)
e1 = Entry(L1,width=50, bd=5)
e1.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)

L2 = Label(master, text='password').grid(row=1)
e2 = Entry(L2,width=50, bd=5)
e2.grid(row=1,column=1,padx=2,pady=2,sticky='we',columnspan=25)

b1 = Button(master, text='Submit', command = write).grid(row=3, column = 5)

#L1.pack()
#e1.pack()
#L2.pack()
#e2.pack()
#b1.pack()
mainloop()


