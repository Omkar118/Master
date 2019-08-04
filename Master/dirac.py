import ftplib
import tkinter


window = tkinter.Tk()
window.title("FTP Client")
window.geometry("1000x600")

ftp = ftplib.FTP("192.168.0.26")
ftp.login("rushikesh", "rushi123")

libox_serverdir = tkinter.Listbox(window,width=40,height=14)

def dir():
 libox_serverdir.insert(0,"--------------------------------------------")
#dirlist = []
 dirlist = ftp.nlst()
 for item in dirlist:
      libox_serverdir.insert(0, item)

 libox_serverdir.place(x=700,y=165)



print("File List:")
files = ftp.dir()
print(files)

