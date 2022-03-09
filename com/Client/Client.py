# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:20:30 2022

@author: Carlos Montoya
"""

import socket
import re

currentHostName = socket.gethostname()
currentIP = socket.gethostbyname(currentHostName)

fPref = open("../../preferences.pbtxt",'r')
lstLines = fPref.readlines()
dataImport = re.findall('[A-Z+0-9+,+.]+', lstLines[2])
dataImport = ''.join(str(dataImport[0])).split(",")
ip = dataImport[1]

host = ip
port = 64307

dataset = []
registers = open('registers.txt', 'w')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))


print("Current PC: "+currentHostName +'\nIP:'+currentIP)
print("\nClient Listen...\n")

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
