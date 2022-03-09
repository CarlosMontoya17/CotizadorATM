# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:20:30 2022

@author: Carlos Montoya
"""

import socket
import threading

currentHostName = socket.gethostname()
currentIP = socket.gethostbyname(currentHostName)

fPref = open("",'r')



host = "192.168.100.60"
port = 64307

dataset = []
registers = open('registers.txt', 'w')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

print(f"Current PC: "+currentHostName +'\nIP:'+currentIP)
print(f"\nClient Listen...\n")

while True:
    recv = client.recv(1024).decode(encoding="ascii", errors="ignore")
    dataRecv = str(recv).split(';')
    dataset.append(dataRecv)
    numberId = dataRecv[0]
    addressId = dataRecv[1]
    numberEnd = dataRecv[2]
    if addressId == currentIP:
        print('New data! >')
        print('ID: '+numberId)
        print('IP: '+addressId)
        print('EACH: '+numberEnd+'\n')
        registers.write(numberId)
        registers.write("\n")
        if len(dataset) == int(numberEnd):
            registers.close()
            print("All data recived successfully! Closing...")
            client.close()
            break

client.close()
