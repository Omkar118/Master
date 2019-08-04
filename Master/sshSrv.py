
import os
import time

import spur

timestamp=str(time.strftime("%Y%m%d-%H%M%S"))

shell = spur.SshShell(hostname="192.168.0.27", username="onkar", password="RetroReadytoroll")

os.system("scp /home/onkar/Desktop/opencv.zip %s"%(timestamp))

inFile="/home/onkar/Desktop/opencv.zip"
try:
    result = shell.run(["ls", inFile])

    print ("Pass")
except:
    print ("Fail")
