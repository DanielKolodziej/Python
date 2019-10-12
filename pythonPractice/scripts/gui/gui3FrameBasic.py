from tkinter import *

#create the window
root = Tk()

#modify root window
root.title("My Gui")
root.geometry("200x100")

app=Frame(root)
app.grid()
label=Label(app,text="Welcome!");

label.grid()

button1=Button(app,text="Click me")
button1.grid()

button2=Button(app)
button2.grid()
button2.configure(text="Exit")

button3=Button(app,text="Submit")
Button3["text"]="test"
button3.grid()


#kick off the event loop
root.mainloop();


