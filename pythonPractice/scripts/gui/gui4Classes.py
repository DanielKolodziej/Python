from tkinter import *

class Application(Frame):
  #gui with buttons
  
  def __init__(self,master):
    #initialize frame
    Frame.__init__(self,master)
    self.grid()
    self.button_clicks=0 #button click counter
    self.create_widgets()

  def create_widgets(self):
    #create our 2 buttons
    #button1 tracks the number of clickers
    self.button1=Button(self)
    self.button1=Button(self,text="Total clicks: 0")
    self.button1["command"]=self.update_click_counter 
    self.button1.grid()

    #exit button
    self.button3=Button(self)
    self.button3.grid()
    self.button3.configure(text="Exit")
    self.button3["command"]=self.quit # create binder

  #create handler for button 1 
  def update_click_counter(self):
    """show total increased button counts & display new total"""
    self.button_clicks+=1
    self.button1["text"]="Total Clicks: " + str(self.button_clicks)
    
  #create handler for button 3 
  def quit(self):
    self.master.destroy();

#create the window
root = Tk()

#modify root window
root.title("My Gui with Class")
root.geometry("200x85")

root=Application(root) #instantiate class to show off our widgets!

#kick off the event loop
root.mainloop();


