#Daniel Kolodziej
#ITMD 413 Lab 8
#4/18/2018
from tkinter import *
from contacts  import *
import myDatabasefile
from tkinter import messagebox
import os

contacts = []
currentID = 0

#selects row to be loaded
def selection () :
    print ("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])

#function to utilize addContact from myDatabasefile
def addContact () :
    name = nameVar.get()
    phone = phoneVar.get()
    #checks if empty fields
    if (name == "" or phone == ""):
        name = None
        phone = None
        myDatabasefile.insertContact(name, phone)
        messagebox.showinfo("Error", "Invalid")
    else:
        myDatabasefile.insertContact(name, phone)
        print("Contact " + name + " added...")
        setList()
        messagebox.showinfo("Add", "Contact " + name + " added successfuly")

#function to utilize updateContact from myDatabasefile
def updateContact() :
    #assign variables from contact records
    id, name, phone = contacts[selection()]
    namedb = nameVar.get()
    phonedb = phoneVar.get()
    #checks if empty fields
    if (namedb == "" or phonedb == ""):
        namedb = None
        phonedb = None
        myDatabasefile.updateContact(id, namedb, phonedb)
    else:
        myDatabasefile.updateContact(id, namedb, phonedb)
        setList()
        messagebox.showinfo("Updated", "User " + namedb + " has been updated")

#function to utilize deleteContact from myDatabasefile
def deleteContact() :
    #messagebox in order for user to confirm the delete action
    try:
        if messagebox.askokcancel("Warning", "User will be deleted"):
            myDatabasefile.deleteContact(currentID)
            print("Contact deleted")
    except:
        messagebox.showwarning("Delete", "User has been deleted")
    setList()
    
#function to load contacts from myDatabasefile   
def loadContact() :
    id, name, phone = contacts[selection()]
    global currentID
    currentID = id
    nameVar.set(name)
    phoneVar.set(phone)

#builds the gui interface
def buildFrame() :
    global nameVar, phoneVar, select
    root = Tk()
    root.title("My Contact List")

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    phone= Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame1 = Frame(root)       # add a row of buttons
    frame1.pack()
    btn1 = Button(frame1,text=" Add  ",command=addContact)
    btn2 = Button(frame1,text="Update",command=updateContact)
    btn3 = Button(frame1,text="Delete",command=deleteContact)
    btn4 = Button(frame1,text=" Load ",command=loadContact)
    btn1.pack(side=LEFT); btn2.pack(side=LEFT)
    btn3.pack(side=LEFT); btn4.pack(side=LEFT)

    frame1 = Frame(root)       # allow for selection of names
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH)
    return root

#uses readContacts from myDatabasefile to retrieve records and sort
def setList():
    global contacts
    contacts = myDatabasefile.readContacts() #call method in myDatabasefile.py
    #Sort the list
    contacts.sort(key = lambda x : x[1])
    #Delete all elements from the select element
    select.delete(0, END)
    #Insert each name from the list to end of select element
    for id, name, phone in contacts:
        select.insert(END, name)

#calls the createTable in order to check if initial data present, create table
def loadInitialData():
    myDatabasefile.createTable()


root = buildFrame()
loadInitialData()
setList ()

root.mainloop()

