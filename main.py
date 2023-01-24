from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("My App")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.frame = Frame(self.master)
        self.frame.pack()

        self.button = Button(self.frame, text="Click Me", command=self.click)
        self.button.pack()

    def click(self):
        print("Clicked")

