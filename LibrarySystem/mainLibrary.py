from tkinter import *
from tkinter import messagebox
import sqlite3
from add import *
from viewBooks import *
from issue import *
from returnBooks import *

# create a window
window = Tk()
window.title("Library System")
window.minsize(width=600, height=500)
window.geometry("800x500")

# create a label
label = Label(window, text="Library System", font=("Arial", 20))
label.pack(pady=10, padx=10)

# create a button to add books
add_button = Button(window, text="Add Books", command=None)
add_button.pack(pady=10, padx=10)

# create a button to view books
view_button = Button(window, text="View Books", command=None)
view_button.pack(pady=10, padx=10)

# create a button to issue books
issue_button = Button(window, text="Issue Books", command=None)
issue_button.pack(pady=10, padx=10)

# create a button to return books
return_button = Button(window, text="Return Books", command=None)
return_button.pack(pady=10, padx=10)

# create a button to exit
exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=10, padx=10)

window.mainloop()
