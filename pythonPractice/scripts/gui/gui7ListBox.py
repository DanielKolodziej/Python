from tkinter import *
 
#http://www.tutorialspoint.com/python/tk_listbox.htm
def immediately(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print ('You selected item %d: "%s"' % (index, value)) #single selection
    print ('You selected items: %s'%[w.get(int(i)) for i in w.curselection()]) #mult. selector


top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()


Lb1.bind('<<ListboxSelect>>', immediately)
top.mainloop()
