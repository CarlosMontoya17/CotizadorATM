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
idsFile = open("1.txt", 'r')
ids = idsFile.readlines()
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
try:
    connection = psycopg2.connect(user="root", password="Admin$2021$A", host="144.126.136.14", port="5432", database="test")
    cursor = connection.cursor()
    for id in range(len(ids)):
        cursor.execute('SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(base)+'" WHERE "id" = '+str(ids[id])+'AND "aplica" IS NULL')
        score = cursor.fetchall()
        All.append(score)
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
for i in range(len(list(All))):
    record.append(list(All[i][0]))
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
                    url = "https://www.mi-portal-infonavit.com/checar-puntos?nss=0"+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2])+"&base="+str(base) 
                elif len(record[index][0]) == 11:
                    url = "https://www.mi-portal-infonavit.com/checar-puntos?nss="+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2])+"&base="+str(base)
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
        os.system("timeout 10")
        os.startfile("reset1.cmd")
        break
