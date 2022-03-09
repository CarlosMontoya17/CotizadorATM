# -*- coding: utf-8 -*-
"""
FOR TODOS ESTADOS
By Carlos Montoya
"""
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import messagebox, simpledialog
import re



def openRanges():
    filetypes = (
        ('text files', '*.pbtxt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    try:
        fData = open(filename, 'r')
        list_of_lines = fData.readlines()
        rCh = re.findall('[0-9+-]+', list_of_lines[0])
        rOp = re.findall('[0-9+-]+', list_of_lines[1])
        rEd = re.findall('[0-9+-]+', list_of_lines[2])
        rVi = re.findall('[0-9+-]+', list_of_lines[2])
        rChrome= ''.join(str(rCh[0])).split("-")
        rOpera = ''.join(str(rOp[0])).split("-")
        rEdge = ''.join(str(rEd[0])).split("-")
        rVivaldi = ''.join(str(rVi[0])).split("-")
        minValueCh = rangeOneMin.insert(END,rChrome[0])
        maxValueCh = rangeOneMax.insert(END,rChrome[1])
        minValueOp = rangeTwoMin.insert(END,rOpera[0])
        maxValueOp = rangeTwoMax.insert(END,rOpera[1])
        minValueEd = rangeThreeMin.insert(END,rEdge[0])
        maxValueEd = rangeThreeMax.insert(END,rEdge[1])
        minValueVi = rangeFourMin.insert(END,rVivaldi[0])
        maxValueVi = rangeFourMax.insert(END,rVivaldi[1])
    except:
        messagebox.showerror("ERROR","Verify your ranges data")




def savePreferenes():
    entity = currentEntity.get()
    timesm = times.get()
    prority = currentPrority.get()
    ip = setIp.get()
    try:
        f = open("preferences.pbtxt",'w')
        f.writelines(str(entity)+'\n'+str(timesm)+'\n'+str(prority)+','+str(ip))
        f.close()
        messagebox.showinfo("OK","Save preferences successfully")
    except:
        messagebox.showerror("Error","Error saving preferences")
    
    

def preferences():
    global currentEntity,times, currentPrority, setIp
    t1 = Toplevel(window)
    t1.geometry('370x220')
    t1.resizable(False,False)
    t1.title("Preferences...")
    t1.focus_set()
    t1.grab_set()
    t1.transient(master=window)
    #Entity
    labelEntity = Label(t1, text= "Select entity: ", font=("Arial",10), fg="black")
    labelEntity.place(x=105, y=25)
    currentEntity = StringVar(t1)
    currentEntity.set("CHIAPAS")
    listEntity = OptionMenu(t1, currentEntity, "CHIAPAS", "VERACRUZ", "NUEVO-LEON")
    listEntity.place(x=190, y=20)
    #Replay
    labelReplay = Label(t1, text= "Replay?: ", font=("Arial",10), fg="black")
    labelReplay.place(x=45, y=55)
    setTimes = StringVar(t1)
    times = Entry(t1, textvariable=setTimes, width=18) 
    times.place(x=25, y=80)
    #Priority
    labelPriority = Label(t1, text= "Priority: ", font=("Arial",10), fg="black")
    labelPriority.place(x=250, y=55)
    currentPrority = StringVar(t1)
    currentPrority.set("OFF")
    listPriority = OptionMenu(t1, currentPrority, "OFF","SERVER", "CLIENT")
    listPriority.place(x=250, y=80)
    labelIp = Label(t1, text= "Set IP of Server: ", font=("Arial",10), fg="black")
    labelIp.place(x=250, y=120)
    setIp = StringVar(t1)
    ip = Entry(t1, textvariable=setIp, width=18) 
    ip.place(x=250, y=145)    
    #Import Preferences
    btn = Button(t1, text="Import Preferences", bg="white", fg="black", command=selectFilePreferences)
    btn.place(x=120, y=190)
    btn = Button(t1, text="SAVE", bg="white", fg="black", command=savePreferenes)
    btn.place(x=255, y=190)
    btn = Button(t1, text="CLOSE", bg="white", fg="black", command=t1.destroy)
    btn.place(x=315, y=190)
    t1.wait_window(t1)
    
def about():
    t1 = Toplevel(window, bg='white')
    t1.geometry('230x75')
    t1.resizable(False,False)
    t1.title("About...")
    t1.focus_set()
    t1.grab_set()
    t1.transient(master=window)
    Info = Label(t1, text='Cotizador ATM\nGrupo RYC\n@Author Carlos Uriel Montoya Gutiérrez\nVer. 2.0',fg="black")
    Info.place(x=10, y=10)
    t1.wait_window(t1)

def selectFilePreferences():
    try:
        filetypes = (
            ('text files', '*.pbtxt'),
            ('All files', '*.*')
        )
    
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        fData = open(filename, 'r')
        list_of_lines = fData.readlines()
        aEntity = re.findall('[A-Z]+', list_of_lines[0])
        aReplay = re.findall('[0-9]+', list_of_lines[1])
        aPriority = re.findall('[A-Z+0-9+.]+', list_of_lines[2])
        entity = ''.join(str(aEntity[0]))
        replay = ''.join(str(aReplay[0]))
        priority = ''.join(str(aPriority[0]))
        ip = ''.join(str(aPriority[1]))
        # minV = ''.join(str(e[0]))
        currentEntity.set(entity)
        times.insert(END, str(replay))
        currentPrority.set(str(priority))
        setIp.set(str(ip))
    except:
        messagebox.showerror("ERROR","Verify your preferences data")
    


def verifyData():
    try:
        fData = open('preferences.pbtxt', 'r')
        list_of_lines = fData.readlines()
        aEntity = re.findall('[A-Z+-]+', list_of_lines[0])
        entity = ''.join(str(aEntity[0]))
        if entity == 'CHIAPAS':
            return "mainch"
        elif entity == 'VERACRUZ':
            return "mainvr"
        elif entity == 'NUEVO-LEON':
            return "mainnl"
        else:
            return ""
    except:
        messagebox.showerror("ERROR","Set preferences")



def sendChrome():
    global minValueCh, maxValueCh
    minValueCh = rangeOneMin.get()
    maxValueCh = rangeOneMax.get()
    entity = verifyData()
    
    if (minValueCh != "") and (maxValueCh != ""):
        nameFileOne = 'rangeOne.txt'
        textRange1 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(entity)+'" WHERE "id" >=  '+str(minValueCh)+' AND "id" <= '+str(maxValueCh)+' AND "aplica" IS NULL'
        fPriory = open("com/readyPriority.pbtxt", 'w')
        fPriory.writelines("FALSE")
        fPriory.close()
        file = open(nameFileOne,'w')
        file.write(textRange1)
        file.close()
        os.startfile("AppChrome.cmd")
        RangeMax = Label(text= "Revisa los campos vacios Chrome", font=("Arial",10), bg="#213141", fg="#213141")
        RangeMax.place(x=105, y=280)
        cFile = open("com/currentTimes.pbtxt",'w')
        cFile.write("0")
        cFile.close()
        
    else:
        RangeMax = Label(text= "Revisa los campos vacios Chrome", font=("Arial",10), bg="#213141", fg="red")
        RangeMax.place(x=105, y=280)
    
def sendOpera():
    global minValueOp, maxValueOp
    minValueOp = rangeTwoMin.get()
    maxValueOp = rangeTwoMax.get()
    entity = verifyData()
    if (minValueOp != "") and (maxValueOp != ""):
        nameFileTwo = 'rangeTwo.txt'
        textRange2 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(entity)+'" WHERE "id" >=  '+str(minValueOp)+' AND "id" <= '+str(maxValueOp)+' AND "aplica" IS NULL'
        fPriory = open("com/readyPriority.pbtxt", 'w')
        fPriory.writelines("FALSE")
        fPriory.close()
        file = open(nameFileTwo,'w')
        file.write(textRange2)
        file.close()
        os.startfile("AppOpera.cmd")
        RangeMax = Label(text= "Revisa los campos vacios Opera", font=("Arial",10), bg="#213141", fg="#213141")
        RangeMax.place(x=105, y=280)
        cFile = open("com/currentTimes.pbtxt",'w')
        cFile.write("0")
        cFile.close()
    else:
        RangeMax = Label(text= "Revisa los campos vacios Opera", font=("Arial",10), bg="#213141", fg="red")
        RangeMax.place(x=105, y=280)
    
def sendEdge():
    global minValueEd, maxValueEd
    minValueEd = rangeThreeMin.get()
    maxValueEd = rangeThreeMax.get()
    entity = verifyData()
    if (minValueEd != "") and (maxValueEd != ""):
        nameFileThree = 'rangeThree.txt'
        textRange3 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(entity)+'" WHERE "id" >=  '+str(minValueEd)+' AND "id" <= '+str(maxValueEd)+' AND "aplica" IS NULL'
        fPriory = open("com/readyPriority.pbtxt", 'w')
        fPriory.writelines("FALSE")
        fPriory.close()
        file = open(nameFileThree,'w')
        file.write(textRange3)
        file.close()
        os.startfile("AppEdge.cmd")
        RangeMax = Label(text= "Revisa los campos vacios Edge", font=("Arial",10), bg="#213141", fg="#213141")
        RangeMax.place(x=105, y=280)
        cFile = open("com/currentTimes.pbtxt",'w')
        cFile.write("0")
        cFile.close()
    
    else:
        RangeMax = Label(text= "Revisa los campos vacios Edge", font=("Arial",10), bg="#213141", fg="red")
        RangeMax.place(x=105, y=280)

def sendVivaldi():
    global minValueVi, maxValueVi
    minValueVi = rangeFourMin.get()
    maxValueVi = rangeFourMax.get()
    entity = verifyData()
    if (minValueVi != "") and (maxValueVi != ""):
        nameFileFour = 'rangeFour.txt'
        textRange4 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "'+str(entity)+'" WHERE "id" >=  '+str(minValueVi)+' AND "id" <= '+str(maxValueVi)+' AND "aplica" IS NULL'
        fPriory = open("com/readyPriority.pbtxt", 'w')
        fPriory.writelines("FALSE")
        fPriory.close()
        file = open(nameFileFour,'w')
        file.write(textRange4)
        file.close()
        os.startfile("AppVivaldi.cmd")  
        RangeMax = Label(text= "Revisa los campos vacios Vivaldi", font=("Arial",10), bg="#213141", fg="#213141")
        RangeMax.place(x=105, y=280)
        cFile = open("com/currentTimes.pbtxt",'w')
        cFile.write("0")
        cFile.close()
    
    else:
        RangeMax = Label(text= "Revisa los campos vacios Vivaldi", font=("Arial",10), bg="#213141", fg="red")
        RangeMax.place(x=105, y=280)
    
def sendAll():
    minValueCh = rangeOneMin.get()
    maxValueCh = rangeOneMax.get()
    minValueOp = rangeTwoMin.get()
    maxValueOp = rangeTwoMax.get()
    minValueEd = rangeThreeMin.get()
    maxValueEd = rangeThreeMax.get()
    minValueVi = rangeFourMin.get()
    maxValueVi = rangeFourMax.get()
    if (minValueVi != "") and (maxValueVi != "") and (minValueEd != "") and (maxValueEd != "") and (minValueOp != "") and (maxValueOp != "") and (minValueCh != "") and (maxValueCh != "") :
        sendChrome()
        sendOpera()
        sendEdge()
        sendVivaldi()
        RangeMax = Label(text= "Revisa los campos vacios", font=("Arial",10), bg="#213141", fg="#213141")
        RangeMax.place(x=105, y=280)
    else:
        RangeMax = Label(text= "Revisa los campos vacios", font=("Arial",10), bg="#213141", fg="red")
        RangeMax.place(x=105, y=280)
        
        
def add1k():
    minValueCh = rangeOneMin.insert(END,"000")
def add2k():
    minValueOp = rangeTwoMin.insert(END,"000")
def add3k():
    minValueEd = rangeThreeMin.insert(END,"000")
def add4k():
    minValueVi = rangeFourMin.insert(END,"000")
    
    
    
def add1kM():
    maxValueCh = rangeOneMax.insert(END,"000")
def add2kM():
    maxValueOp = rangeTwoMax.insert(END,"000")
def add3kM():
    maxValueEd = rangeThreeMax.insert(END,"000")
def add4kM():
    maxValueVi = rangeFourMax.insert(END,"000")

    
    
#GUI/CRUD
window = Tk()
window.geometry("450x350")
window.title("COTIZADOR ATM -by CarlosMontoya")

window.iconbitmap('img/night.ico')

               
window.resizable(False,False)
window.config(background="#213141")
mainTitle = Label(text= "PANEL DE CONTROL", font=("Arial",10), bg="#213141", fg="white")
mainTitle.pack()


buttonAddk1 = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add1k)
buttonAddk1.place(x=15, y=65)
buttonAddk2 = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add2k)
buttonAddk2.place(x=15, y=110)
buttonAddk3 = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add3k)
buttonAddk3.place(x=15, y=155)
buttonAddk3 = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add4k)
buttonAddk3.place(x=15, y=200)

buttonAddk1M = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add1kM)
buttonAddk1M.place(x=175, y=65)
buttonAddk2M = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add2kM)
buttonAddk2M.place(x=175, y=110)
buttonAddk3M = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add3kM)
buttonAddk3M.place(x=175, y=155)
buttonAddk3M = Button(window, text="+000", bg="white", fg="black",font=("Arial",6), command=add4kM)
buttonAddk3M.place(x=175, y=200)


img = PhotoImage(file="./img/GrupoRYC.png")
icon = Label(window,image=img).place(x=50,y=250)

RangeMin = Label(text= "Rango Minimo: ", font=("Arial",10), bg="#213141", fg="white")
RangeMin.place(x=40, y=30)


RangeMax = Label(text= "Rango Maximo: ", font=("Arial",10), bg="#213141", fg="white")
RangeMax.place(x=200, y=30)




#Nav
menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

help_menu = Menu(
    menubar,
    tearoff=0
)


menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_cascade(
    label="Help",
    menu=help_menu
)

file_menu.add_command(label='Open range',
                      command=openRanges
)


file_menu.add_command(
    label='Preferences',
    command = preferences
)
file_menu.add_separator()

file_menu.add_command(
    label='Exit',
    command=window.destroy,
)


help_menu.add_command(
    label='About...',
    command=about
)



#Chrome
setRangeOneMin = StringVar()
setRangeOneMax = StringVar()
rangeOneMin = Entry(textvariable=setRangeOneMin, width=18)
rangeOneMax = Entry(textvariable=setRangeOneMax, width=18)
rangeOneMin.place(x=40, y=65)
rangeOneMax.place(x=200, y=65)
buttonChrome = Button(window, text="Correr Chrome", bg="white", fg="black", command=sendChrome)
buttonChrome.place(x=340, y=60)



#Opera
setRangeTwoMin = StringVar()
setRangeTwoMax = StringVar()
rangeTwoMin = Entry(textvariable=setRangeTwoMin, width=18)
rangeTwoMax = Entry(textvariable=setRangeTwoMax, width=18)
rangeTwoMin.place(x=40, y=110)
rangeTwoMax.place(x=200, y=110)
buttonOpera = Button(window, text="Correr Opera", bg="white", fg="black", command=sendOpera)
buttonOpera.place(x=340, y=105)


#Edge

setRangeThreeMin = StringVar()
setRangeThreeMax = StringVar()
rangeThreeMin = Entry(textvariable=setRangeThreeMin, width=18)
rangeThreeMax = Entry(textvariable=setRangeThreeMax, width=18)
rangeThreeMin.place(x=40, y=155)
rangeThreeMax.place(x=200, y=155)
buttonEdge = Button(window, text="Correr Edge", bg="white", fg="black", command=sendEdge)
buttonEdge.place(x=340, y=150)

#Vivaldi
setRangeFourMin = StringVar()
setRangeFourMax = StringVar()
rangeFourMin = Entry(textvariable=setRangeFourMin, width=18)
rangeFourMax = Entry(textvariable=setRangeFourMax, width=18)
rangeFourMin.place(x=40, y=200)
rangeFourMax.place(x=200, y=200)
buttonEdge = Button(window, text="Correr Vivaldi", bg="white", fg="black", command=sendVivaldi)
buttonEdge.place(x=340, y=195)

#Submit All
buttonAll = Button(window, text="Correr Todo", bg="white", fg="black", command=sendAll)
buttonAll.place(x=175, y=250)


RangeMax = Label(text= "Ver -2.0- by Carlos Montoya", font=("Arial",6), bg="#213141", fg="white")
RangeMax.place(x=355, y=330)





window.mainloop()


#---EXPORT DATA

"""
#Export Data for Opera
nameFileTwo = 'rangeTwo.txt'
textRange2 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "imss-nl-depurado" WHERE "id" >=  '+str(minValueOp)+' AND "id" <= '+str(maxValueOp)
file = open(nameFileTwo,'w')
file.write(textRange2)
file.close()


#Export Data for Edge
nameFileThree = 'rangeThree.txt'
textRange3 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "imss-nl-depurado" WHERE "id" >=  '+str(minValueEd)+' AND "id" <= '+str(maxValueEd)
file = open(nameFileThree,'w')
file.write(textRange3)
file.close()

#Export Data for Vivaldi
nameFileFour = 'rangeFour.txt'
textRange4 = 'SELECT "num_seg_so", "curp", "id", "nom_aseg" FROM "imss-nl-depurado" WHERE "id" >=  '+str(minValueVi)+' AND "id" <= '+str(maxValueVi)
file = open(nameFileFour,'w')
file.write(textRange4)
file.close()

#Process

os.startfile("AppOpera.cmd")
os.startfile("AppEdge.cmd")
os.startfile("AppVivaldi.cmd")
"""