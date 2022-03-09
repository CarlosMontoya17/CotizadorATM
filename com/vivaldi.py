import time
import webbrowser
import os
import psycopg2
from psycopg2 import Error
import sys
import re
import pygetwindow as gw
from getpass import getuser

index = 0
record = []
All = []
name_user = getuser()
sys.setrecursionlimit(18000)
nameFile = '../rangeFour.txt'
file = open(nameFile,'r')
instruction = file.read()

cachePath = '../cache/cacheVivaldi.pbtxt'
def start():
    global minV, maxV
    file = open(nameFile,'r')
    list_of_lines = file.readlines()
    e = re.findall('[0-9]+', list_of_lines[0])
    minV = ''.join(str(e[0]))
    maxV = ''.join(str(e[1]))
    print('Cache learning...')
    init('data')

def cache(index):
    global cachePath
    cachePath = '../cache/cacheVivaldi.pbtxt'
    file = open(cachePath,'w')
    cache = int(minV)+index-1 
    file.writelines(str(cache)+'\n'+maxV)


def browser(url):
    navPath = "C:/Program Files/Vivaldi/Application/vivaldi.exe"
    webbrowser.register('vivaldi', None, webbrowser.BackgroundBrowser(navPath))
    webbrowser.get('vivaldi').open(url)        

def init(data):
    time.sleep(1)    
    global index, record
    if index <= len(record)-1:
        if str(record[index][1]) != '000000000000000000' and str(record[index][1]) != '0':
            if int(record[index][1][4:6]) < 21:
                fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/20'+record[index][1][4:6]
            else:
                fecha = record[index][1][8:10]+'/'+record[index][1][6:8]+'/19'+record[index][1][4:6]
            if record[index][1][8:10]+'/'+record[index][1][6:8] != '29/02':
                url = "https://www.mi-portal-infonavit.com/checar-puntos?nss="+str(record[index][0])+"&date="+str(fecha)+"&name="+str(record[index][3])+"&id="+str(record[index][2])
				#chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
                browser(url)
                print(index+1)
                index +=1
                time.sleep(30)
                os.system("taskkill /im vivaldi.exe /f")
                cache(index)
                init('data')
            else:
                print(index)
                index +=1
                cache(index)
                init("data")
        else:
            print(index+1)
            index +=1
            cache(index)
            init("data")
    else:
        file = open(cachePath,'w')
        file.writelines('Terminado'+'\n@Author Carlos Montoya \n Grupo RYC')
        file.close()
        print('Terminado..')


try:
    connection = psycopg2.connect(user="root", password="Admin$2021$A", host="144.126.136.14", port="5432", database="test")
    cursor = connection.cursor()
    cursor.execute(instruction)
    record = cursor.fetchall()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


start()