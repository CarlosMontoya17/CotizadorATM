# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:58:30 2022

@author: Carlos Montoya
"""

import socket
import threading
import psycopg2
from psycopg2 import Error
import math
import time
import re
import os

currentHostName = socket.gethostname()
currentIP = socket.gethostbyname(currentHostName)

file = open('../name.txt','r')
rd = file.read()

base = ""
fPref = open("../../preferences.pbtxt",'r')
lstLines = fPref.readlines()
municipality = re.findall('[A-Z]+', lstLines[0])
municipality = ''.join(str(municipality[0]))
if str(municipality) == "CHIAPAS":
    base = "mainch"
elif str(municipality) == "VERACRUZ":
    base = "mainvr"
elif str(municipality) == "NUEVO-LEON":
    base = "mainnl"
host = currentIP
port = 64307
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print("Server is running...")
state = False
readyDivided = 0
clients = []
ids = []
record = []
score = []
i = 0
idsReady = []
registers = open('registers.txt', 'w')
try:
    connection = psycopg2.connect(user="root", password="Admin$2021$A", host="144.126.136.14", port="5432", database="test")
    cursor = connection.cursor()
    cursor.execute('SELECT "id" FROM "'+base+'" WHERE "priority" = %s AND "aplica" IS NULL',[rd])
    record = cursor.fetchall()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
def acceptAll():
    global state
    while True:
        client, address = server.accept()
        try:
            clients.append(client)
            ids.append(address[0])
            print(address[0]+"> Are now connected!")
        except:
            client.close()
def sendMessage():
    global divideEach, state, i, score
    print("15 sec to start...")
    time.sleep(15)
    while True:
        try:
            if state == False:
                divideEach = len(record)/(len(clients)+1)
                divideEach = math.floor(divideEach)
                print("Aprox assigned: "+ str(divideEach) +" to each one, total clients: "+ str(len(clients)) + " Total Data: " +str(len(record)))
                state=True
            elif state == True:
                print("Distributing...")
                if record != None and record != []:
                    
                    for indexClient in range(len(clients)):
                        print('[Wait please]Sending... --> '+str(ids[indexClient]))
                        for data in range(divideEach):
                            try:
                                currentNumber = list(record[0])
                                currentNumber = currentNumber[0]
                                print('ID SEND: '+str(currentNumber)+", Data: "+str(data+1)+'/'+str(divideEach))
                                sendValue = str(currentNumber)+';'+str(ids[indexClient])+';'+str(divideEach)+';'
                                time.sleep(0.04)
                                clients[indexClient].send(str(sendValue).encode(encoding="ascii", errors="ignore"))
                                record.pop(0)
                            except:
                                currentNumber = list(record)
                                sendValue = str(currentNumber)+';'+str(ids[indexClient])+';'+str(divideEach)+';'
                                time.sleep(0.04)
                                clients[indexClient].send(str(sendValue).encode(encoding="ascii", errors="ignore"))
                                record.pop()
                    if record != None and record != []:
                        print('[Wait please]Seting local...')
                        currentNumber = list(record)
                        eachBrow = len(currentNumber)/4
                        eachBrow = math.ceil(eachBrow)
                        for a in range(3):
                            datasetBin = open(str(a+1)+'.txt','w')
                            print("Browser "+str(a+1))
                            for b in range(eachBrow):
                                datasetBin.write(str(currentNumber[0][0])+'\n')
                                print(currentNumber[0][0])
                                currentNumber.pop(0)
                            datasetBin.close()
                        lastBrow = open('4.txt', 'w')
                        print("Browser 4")
                        for a in range(len(currentNumber)):
                            lastBrow.write(str(currentNumber[0][0])+'\n')
                            print(currentNumber[0][0])
                            currentNumber.pop(0)
                        lastBrow.close()
                        for n in range(4):
                            os.startfile("start"+str(n+1)+".cmd")
                        server.close()
                        break
                    else:
                        server.close()
                        break
        except:
            server.close()
            break

snd = threading.Thread(target=sendMessage)
snd.start()

acpt = threading.Thread(target=acceptAll)
acpt.start()


