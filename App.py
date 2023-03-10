import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")


class app(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setting up the window size, title and icon
        self.title("Library")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.minsize(width=800, height=500)


        # Configure the grid for the window of 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create navigation frame
        self.navigation_frame = ctk.CTkFrame(self)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        # create the widgets for the navigation frame
        self.home_button = ctk.CTkButton(self.navigation_frame, text="Home", command=None)
        self.home_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        self.books_button = ctk.CTkButton(self.navigation_frame, text="Books", command=None)
        self.books_button.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        self.members_button = ctk.CTkButton(self.navigation_frame, text="Members", command=None)
        self.members_button.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

        self.issues_button = ctk.CTkButton(self.navigation_frame, text="Issues", command=None)
        self.issues_button.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)

        self.logout_button = ctk.CTkButton(self.navigation_frame, text="Logout", command=None)
        self.logout_button.grid(row=5, column=0, sticky="nsew", pady=10, padx=10)

        # Create the main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent", bg_color="transparent")
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_frame_label = ctk.CTkLabel(self.main_frame, text="Welcome to the Library", font=("Arial", 40))
        self.main_frame_label.grid(row=0, column=0, sticky="nsew", pady=10, padx=20)

        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Create the home frame and hide it




if __name__ == "__main__":
    app = app()
    app.mainloop()
