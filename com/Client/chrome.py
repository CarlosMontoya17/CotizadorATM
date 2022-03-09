import time
import webbrowser
import os
import psycopg2
from psycopg2 import Error
import sys
import re
import csv
import numpy as np

index = 0
record = []
score = []
All = []
sys.setrecursionlimit(18000)

idsFile = open("registers.txt", 'r')
ids = idsFile.readlines()

instruction = ""
cachePath = '../cache/cacheChrome.pbtxt'

preferencesPath = '../../preferences.pbtxt'
prefFile = open(preferencesPath, 'r')

lstLines = prefFile.readlines()
municipality = re.findall('[A-Z]+', lstLines[0])
municipality = ''.join(str(municipality[0]))
if str(municipality) == "CHIAPAS":
    base = "mainch"
elif str(municipality) == "VERACRUZ":
    base = "mainvr"
elif str(municipality) == "NUEVO-LEON":
    base = "mainnl"


entity = ""
replay = 0
connect = "OFF"


try:
    connection = psycopg2.connect(user="root", password="Admin$2021$A", host="144.126.136.14", port="5432", database="test")
    cursor = connection.cursor()
    for id in range(len(ids)):
        cursor.execute('SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(base)+'" WHERE "id" = '+str(ids[id])+'AND "aplica" IS NULL')
        score = cursor.fetchall()
        record.append(score)
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

while True:
    time.sleep(1)
    if index <= len(record)-1:
        if str(record[index][1]) != '000000000000000000' and str(record[index][1]) != '0':
            if int(record[index][1][4:6]) < 21:
                fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/20'+record[index][1][4:6]
            else:
                fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/19'+record[index][1][4:6]
            if record[index][1][8:10]+'/'+record[index][1][6:8] != '29/02':
                if len(record[index][0]) == 10:
                    url = "https://www.mi-portal-infonavit.com/checar-puntos?nss=0"+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2]) 
                elif len(record[index][0]) == 11:
                    url = "https://www.mi-portal-infonavit.com/checar-puntos?nss="+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2])
				    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.open_new_tab(url)
                print(index+1)
                index +=1
                time.sleep(30)
                os.system("taskkill /im chrome.exe /f")
            else:
                print(index)
                index +=1
        else:
            print(index+1)
            index +=1

    else:
        print("Terminado < regresando...")
        takePriory = open("../readyPriority.pbtxt", 'w')
        takePriory.writelines("FALSE")
        takePriory.close()
        os.startfile("sChrome.cmd")
        os.system("pause")
        break

# def start():
#     global minV, maxV, replay, connect, current, entity
#     print('Cache learning...')
#     file = open(nameFile,'r')
#     list_of_lines = file.readlines()
#     e = re.findall('[0-9]+', list_of_lines[0])
#     minV = ''.join(str(e[0]))
#     maxV = ''.join(str(e[1]))
    
    
#     print('Importing preferences...')
#     fPref = open(preferences, 'r')    
#     lstPref = fPref.readlines()
#     enty = re.findall('[A-Z+-]+', lstPref[0])
#     rply = re.findall('[0-9+]+', lstPref[1])
#     cntd = re.findall('[A-Z+,]+', lstPref[2])
#     entity= ''.join(str(enty[0]))
#     if entity == "CHIAPAS":
#         entity = "mainch"
#     elif entity == "VERACRUZ":
#         entity = "mainvr"
#     elif entity == "NUEVO-LEON":
#         entity = "mainvr"
#     replay= ''.join(str(rply[0]))
#     replay = int(replay)
#     connect= ''.join(str(cntd[0])).split(",")
#     fPref.close() 
#     fCurrent = open('currentTimes.pbtxt', 'r') 
#     lstCurrent = fCurrent.readlines()
#     currentArray = re.findall('[0-9]+', lstCurrent[0])
#     current= ''.join(str(currentArray[0]))
#     fCurrent.close() 
#     print("\n< Preferences imported! >\nBase: "+entity+"\nReplay xTimes: "+str(current)+"/"+str(replay)+"\nPriority connect: "+connect[0])
#     init()

# def cache(index):   
#     file = open(cachePath,'w')
#     cache = int(minV)+index-1 
#     file.writelines(str(cache)+'\n'+maxV)

    
# def init():
#     global index, record, Minimize, All, current, scores
#     while True:
#         time.sleep(1)
#         if index <= len(record)-1:
#             if str(record[index][1]) != '000000000000000000' and str(record[index][1]) != '0':
#                 if int(record[index][1][4:6]) < 21:
#                     fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/20'+record[index][1][4:6]
#                 else:
#                     fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/19'+record[index][1][4:6]
#                 if record[index][1][8:10]+'/'+record[index][1][6:8] != '29/02':
#                     url = "https://www.mi-portal-infonavit.com/checar-puntos?nss="+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2])
# 				    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
#                     webbrowser.open_new_tab(url)
#                     print(index+1)
#                     index +=1
#                     time.sleep(30)
#                     os.system("taskkill /im chrome.exe /f")
#                     cache(index)
#                 else:
#                     cache(index)
#                     print(index)
#                     index +=1
#             else:
#                 cache(index)
#                 print(index+1)
#                 index +=1

#         else:
#             file = open(cachePath,'w')
#             file.writelines('Terminado'+'\n@Author Carlos Montoya \n Grupo RYC')
#             file.close()
#             if int(current) != replay:
#                 currentFile = open("currentTimes.pbtxt",'w')
#                 current = int(current)
#                 current+=1
#                 currentFile.write(str(current))
#                 currentFile.close()
#                 os.startfile("sChrome.cmd")
#                 print("Terminado en " + str(current))
#                 break
#             else:
#                 print('Terminado total, xTimes '+str(current)+"/"+str(replay))
#                 os.system("pause")
#                 break





# start()