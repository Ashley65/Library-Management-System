from tkinter import *
from tkinter import messagebox
import sqlite3


# create a window
class app_book:

    def __init__(self):
        self.window = Tk()
        self.window.title("Library System")
        self.window.minsize(width=600, height=500)
        self.window.geometry("800x500")
        self.menu = StringVar(self.window)
        self.menu.set("Genre")

        # create a label
        self.label = Label(self.window, text="New book", font=("Arial", 20))
        self.label.pack(pady=10, padx=10)

        # create a label for book name
        self.book_Title = Label(self.window, text="Book Name")
        self.book_Title.pack()
        self.book_Title_entry = Entry(self.window)
        self.book_Title_entry.pack()

        # create a label for book author
        self.book_Author = Label(self.window, text="Book Author")
        self.book_Author.pack()
        self.book_Author_entry = Entry(self.window)
        self.book_Author_entry.pack()

        # create a label for book status
        self.book_Status = Label(self.window, text="Book Status")
        self.book_Status.pack()
        self.book_Status_entry = Entry(self.window)
        self.book_Status_entry.pack()

        # create a menu for book genre
        self.book_Genre = Label(self.window, text="Book Genre")
        self.book_Genre.pack()
        self.book_Genre = OptionMenu(self.window, self.menu, "Genre", "Fiction", "Non-Fiction", "Biography", "History",
                                     "Poetry", "Science", "Technology", "Mathematics", "Art", "Music", "Drama", "Film",
                                     "Philosophy", "Religion", "Self-Help", "Travel", "Children's", "Young Adult",
                                     "Other")
        self.book_Genre.pack()

        # create a button to add books
        self.add_button = Button(self.window, text="Add Book", command=self.addBook)
        self.add_button.pack(pady=10, padx=10)

        # create a button to exit
        self.exit_button = Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.pack(pady=10, padx=10)

        self.window.mainloop()

    def addBook(self):
        # create a database or connect to one
        if self.book_Title_entry.get() == "":
            messagebox.showerror("Error", "Please enter the book name")
            return
        if self.book_Author_entry.get() == "":
            messagebox.showerror("Error", "Please enter the book author")
            return
        if self.book_Status_entry.get() == "":
            messagebox.showerror("Error", "Please enter the book status")
            return
        if self.menu.get() == "Genre":
            messagebox.showerror("Error", "Please enter the book genre")
            return

        conn = sqlite3.connect("books.db")
        # create a cursor
        c = conn.cursor()

        # insert into table
        c.execute("INSERT INTO books VALUES (:book_Title, :book_Author, :book_Status, :book_Genre)",
                    {
                        "book_Title": self.book_Title_entry.get(),
                        "book_Author": self.book_Author_entry.get(),
                        "book_Status": self.book_Status_entry.get(),
                        "book_Genre": self.menu.get()
                    })



        # clear the text boxes
        self.book_Title_entry.delete(0, END)
        self.book_Author_entry.delete(0, END)
        self.book_Status_entry.delete(0, END)
        self.menu.set("Genre")

        # create a message box
        messagebox.showinfo("Success", "Book added successfully")


if __name__ == "__main__":
    app_book()
