import tkinter as tk
import sqlite3
import hashlib
from tkinter import *
import tkinter.messagebox as messagebox

conn = sqlite3.connect('LoginSystem.db')
c = conn.cursor()


class Login(tk.Frame):

    def __init__(self, master):

        # __init__ function for class Tk
        tk.Frame.__init__(self, master)
        self.master = master
        self.initialseInterfaceL()

    def initialseInterfaceL(self):

        # set the title of the window
        self.master.geometry("400x400")
        self.master.title("Login Page")
        self.master.resizable(False, False)

        # create a frame
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # create a label for the username
        self.usernameLabel = tk.Label(self.frame, text="Username")
        self.usernameLabel.grid(row=0, column=0, sticky=tk.W)

        # create a label for the password
        self.passwordLabel = tk.Label(self.frame, text="Password")
        self.passwordLabel.grid(row=1, column=0, sticky=tk.W)

        # create a entry for the username
        self.usernameEntry = tk.Entry(self.frame)
        self.usernameEntry.grid(row=0, column=1)

        # create a entry for the password
        self.passwordEntry = tk.Entry(self.frame, show="*")
        self.passwordEntry.grid(row=1, column=1)

        # create a button to login
        self.loginButton = tk.Button(self.frame, text="Login", command=self.login)
        self.loginButton.grid(row=2, column=0)

        # create a button to register
        self.registerButton = tk.Button(self.frame, text="Register", command=lambda: self.switch_frame(Register))
        self.registerButton.grid(row=2, column=1)

    def login(self):
        # get the username and password
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        # check if the username and password are correct
        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter username and password")
        else:
            # hash the password
            password = hashlib.sha256(password.encode()).hexdigest()

            # check if the username and password are correct
            c.execute("SELECT * FROM LoginSystem WHERE username = ? AND password = ?", (username, password))
            if c.fetchone() is not None:
                messagebox.showinfo("Success", "Login successful")
            else:
                messagebox.showerror("Error", "Incorrect username or password")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        self.master.switch_frame(new_frame)




class Register(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.initialseInterface()

    def initialseInterface(self):
        # set the title of the window
        self.master.geometry("400x400")
        self.master.title("Register Page")
        self.master.resizable(False, False)

        # create a frame
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # create a label for the username
        self.usernameLabel = tk.Label(self.frame, text="Username")
        self.usernameLabel.grid(row=0, column=0, sticky=tk.W)

        # create a label for the password
        self.passwordLabel = tk.Label(self.frame, text="Password")
        self.passwordLabel.grid(row=1, column=0, sticky=tk.W)

        # create a entry for the username
        self.usernameEntry = tk.Entry(self.frame)
        self.usernameEntry.grid(row=0, column=1)

        # create a entry for the password
        self.passwordEntry = tk.Entry(self.frame, show="*")
        self.passwordEntry.grid(row=1, column=1)

        # create a button to login
        self.registerButton = tk.Button(self.frame, text="Register", command=self.register)
        self.registerButton.grid(row=2, column=0)

        # create a button to register
        self.loginButton = tk.Button(self.frame, text="Login", command=lambda: self.switch_frame(Login))
        self.loginButton.grid(row=2, column=1)


# create the root windo
root = tk.Tk()

# create the main window
app = Login(root)

# start the program
root.mainloop()
