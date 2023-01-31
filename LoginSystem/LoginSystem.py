import tkinter as tk
import sqlite3
import hashlib
from tkinter import *
import tkinter.messagebox as messagebox

conn = sqlite3.connect('LoginSystem.db')
c = conn.cursor()


class Login(tk.Frame):

    def __init__(self, master):

        self.master = master
        self.master.title("login page")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # create a frame for the widgets
        self.frame = Frame(self.master)
        self.frame.pack()

        # create a label for the username
        self.username_label = Label(self.frame, text="Username")
        self.username_label.grid(row=0, column=0, sticky=E)

        # create a label for the password
        self.password_label = Label(self.frame, text="Password")
        self.password_label.grid(row=1, column=0, sticky=E)

        # create a entry for the username
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        # create a entry for the password
        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # create a button to login
        self.login_button = Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0)

        # create a button to register
        self.register_button = Button(self.frame, text="Register", command=lambda: self.master.switch_frame(register))
        self.register_button.grid(row=2, column=1)

    def login(self):
        # get the username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # check if the username and password are correct
        c.execute("SELECT * FROM LoginSystem WHERE username = ? AND password = ?", (username, password))
        if c.fetchall():
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Login Failed")




class register(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Register page")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # create a frame for the widgets
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
