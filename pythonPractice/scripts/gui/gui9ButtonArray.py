from tkinter import *

def main():
    pass

if __name__ == '__main__':
    main()

b={}

app = Tk()
app.grid()

f = Frame(app, bg = "orange", width = 500, height = 500)
f.pack(side=BOTTOM, expand = 1)


def color(x):
    b[c+(r*10)] = Button(f, text=chr(97+c+(r*10)), command=lambda a=c+(r*10): color(a), borderwidth=1,width=5,bg="black")
    b[c+(r*10)].grid(row=r,column=c)


def genABC():
    for r in range(3):
        for c in range(10):
            if (c+(r*10)>25):
                break
            print(c+(r*10))
            b[c+(r*10)] = Button(f, text=chr(97+c+(r*10)), command=lambda a=c+(r*10): color(a), borderwidth=1,width=5,bg="red").grid(row=r,column=c)

genABC()
app.mainloop()
