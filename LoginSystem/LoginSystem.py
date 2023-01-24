from tkinter import *
from tkinter import messagebox
import sqlite3


class LoginSystem:
    def __init__(self, master):
            self.master = master
            self.master.title("Login System")
            self.master.geometry("400x400")
            self.master.resizable(False, False)

            self.frame = Frame(self.master)
            self.frame.pack()

            self.username = StringVar()
            self.password = StringVar()

            self.label_username = Label(self.frame, text="Username")
            self.label_username.grid(row=0, column=0, padx=10, pady=10)

            self.entry_username = Entry(self.frame, textvariable=self.username)
            self.entry_username.grid(row=0, column=1, padx=10, pady=10)

            self.label_password = Label(self.frame, text="Password")
            self.label_password.grid(row=1, column=0, padx=10, pady=10)

            self.entry_password = Entry(self.frame, textvariable=self.password, show="*")
            self.entry_password.grid(row=1, column=1, padx=10, pady=10)

            self.button_login = Button(self.frame, text="Login", command=self.login)
            self.button_login.grid(row=2, column=0, padx=10, pady=10)

            self.button_register = Button(self.frame, text="Register", command=self.register)
            self.button_register.grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        conn = sqlite3.connect("LoginSystem.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (self.username.get(), self.password.get()))
        if c.fetchone() is not None:
            messagebox.showinfo("Login", "Login Successful")
        else:
            messagebox.showerror("Login", "Login Failed")
        conn.close()

    def register(self):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?)", (self.username.get(), self.password.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Register", "Registration Successful")






root = Tk()
login_system = LoginSystem(root)
root.mainloop()