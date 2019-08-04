import sys
from ftplib import FTP
import tkinter as tk


#import Tkinter as ttk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x400+200+200")
        self.title("Upload a Program Flyer to the Library Website")
        self.Appbutton = tk.Button(text='Choose a File to Upload', command = self.launch_file_dialog_box).pack()
        self.Appbutton_FTP = tk.Button(text='Upload File to FTP Server', command =  self.upload_file_to_FTP).pack()
    def launch_file_dialog_box(self):
        self.raw_filename = filedialog.askopenfilename()
    def upload_file_to_FTP(self):
    ##    first thing we do is connect to the ftp host
            ftp = FTP('')
            ftp.login( user = 'onkar', passwd='password')
            ftp.cwd("")
            ftp.set_pasv(False)
            file_name = self.raw_filename
            file = open(file_name, 'rb')
            ftp.storbinary('STOR ' + file_name, file)
            file.quit()
app = App()
app.mainloop()
