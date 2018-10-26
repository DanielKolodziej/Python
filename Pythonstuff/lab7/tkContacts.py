#Daniel Kolodziej
#ITMD-413 Lab 7
#3/31/2018
from tkinter import *
from contacts  import *
from tkinter import messagebox
import os
import time

def selection () :
    print ("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])

def addContact () :
    contactlist.append ([nameVar.get(), phoneVar.get()])
    setList ()

def updateContact() :
    contactlist[selection()]=[nameVar.get(), phoneVar.get()]
    setList ()

def deleteContact() :
    del contactlist[selection()]
    setList ()

def loadContact  () :
    name, phone = contactlist[selection()]
    nameVar.set(name)
    phoneVar.set(phone)

def saveContacts():
    #variables for file and list
    fname = 'contacts.py'
    data = contactlist

    #open contacts file and write list to file
    with open(fname, 'w') as f:
        f.write('contactlist = {}'.format(data))
    #display message saying contacts saved
    var = messagebox.showinfo("Saved" , "Contacts have been saved!")

#exit method if user clicks exit button
def exitApp():
    if (messagebox.askokcancel(title="My Contact List", \
    	    message="Are you want to exit, OK or Cancel") == 1) :
              os._exit(1)

def buildFrame () :
    global nameVar, phoneVar, select
    root = Tk()

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
    frame2 = Frame(root)       # add a row of buttons
    frame2.pack()
    btn1 = Button(frame1,text=" Add  ",command=addContact)
    btn2 = Button(frame1,text="Update",command=updateContact)
    btn3 = Button(frame1,text="Delete",command=deleteContact)
    btn4 = Button(frame1,text=" Load ",command=loadContact)
    #save button with call to saveContacts when clicked
    btn5 = Button(frame1,text="Save",command=saveContacts)
    #exit button with call to exitApp when clicked
    btn6 = Button(frame1,text="Exit",command=exitApp)
    btn1.pack(side=LEFT); btn2.pack(side=LEFT)
    btn3.pack(side=LEFT); btn4.pack(side=LEFT)
    #save button placement
    btn5.pack(side=LEFT)
    #exit buttom placement
    btn6.pack(side=LEFT)
    #exit button center, but overlaps other buttons 
    #btn6.place(relx=0.5, rely=0.5, anchor=CENTER)

    frame1 = Frame(root)       # allow for selection of names
    frame1.pack()
    frame2 = Frame(root)       # add a row of buttons
    frame2.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH)
    return root

def setList () :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)

root = buildFrame()
#makes title "My Contact List"
root.title("My Contact List")
setList ()

root.mainloop()

print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab7')

