import tkinter as tk
import sqlite3
import hashlib
import tkinter.messagebox as messagebox
import random

conn = sqlite3.connect('LoginSystem.db')
c = conn.cursor()


class container(tk.Tk):

    # initialise the function for class app
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Login System")
        self.geometry("500x500")


        

        self.frames = {}
        for F in (LoginPage, RegisterPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame("LoginPage")

    # switch frame function
    def switch_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.login = None
        self.controller = controller
        self.label = tk.Label(self, text="Login Page", font=("Arial", 20))
        self.label.pack(pady=10, padx=10)

        # username label and entry
        self.username = tk.Label(self, text="Username")
        self.username.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()


        self.password = tk.Label(self, text="Password")
        self.password.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # login button
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

        # register button
        self.register_button = tk.Button(self, text="Register", command=lambda: controller.switch_frame("RegisterPage"))
        self.register_button.pack()

        # login function
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


class RegisterPage(tk.Frame):

    # initialise the function for class app
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.register = None
        self.controller = controller
        self.label = tk.Label(self, text="Register Page", font=("Arial", 20))
        self.label.pack(pady=10, padx=10)

        self.username = tk.Label(self, text="Username")
        self.username.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password = tk.Label(self, text="Password")
        self.password.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.email = tk.Label(self, text="Email")
        self.email.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.phone = tk.Label(self, text="Phone")
        self.phone.pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        # register button
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack()

        # back button
        self.back_button = tk.Button(self, text="Back", command=lambda: controller.switch_frame("LoginPage"))
        self.back_button.pack()

        # register function
        def register(self):

            # get the username, password, email and phone
            username = self.usernameEntry.get()
            password = self.passwordEntry.get()
            email = self.emailEntry.get()
            phone = self.phoneEntry.get()

            # check if the username, password, email and phone are correct
            if username == "" or password == "" or email == "" or phone == "":
                messagebox.showerror("Error", "Please enter username, password, email or phone")

            else:
                # hash the password
                password = hashlib.sha256(password.encode()).hexdigest()

                # Randomise the ID number
                ID = random.randint(1, 1000000000)

                # insert the username, password, email and phone into the database
                c.execute("INSERT INTO LoginSystem (username, password, email, phone, ID) VALUES (?, ?, ?, ?)",
                          (username, password, email, phone, ID))
                conn.commit()
                messagebox.showinfo("Success", "Register successful")


if __name__ == "__main__":
    app = container()
    app.mainloop()
