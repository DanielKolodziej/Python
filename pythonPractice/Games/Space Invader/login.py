from tkinter import *
from tkinter import messagebox
import os
import myDatabasefile


#builds the gui interface
def buildFrame() :
    global nameVar
    global root
    root = Tk()
    root.title("My Game Login")
    var=StringVar()
    label = Label(root, textvariable=var)
    var.set("Name:")
    label.pack()
    
    return root

def login():
    filepath = 'spaceInvaders.py'
    os.startfile(filepath)
    root.destroy()
    
root = buildFrame()
root.geometry('{}x{}'.format(400, 400))
root.mainloop()
