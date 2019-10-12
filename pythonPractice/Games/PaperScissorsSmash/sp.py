import tkinter as tk                # python 3

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Game",
                            command=lambda: controller.show_frame("Game"))
        button2 = tk.Button(self, text="Go to HighScores",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()
