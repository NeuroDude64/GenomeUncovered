# © 2026 Ian Vicino. All rights reserved.

import tkinter as tk
# from bio_ide_v2 import BioIDE
from coreConcepts import coreConcepts
from PIL import Image, ImageTk

# Next window to open 
twindow = coreConcepts

# Used because of how pyinstaller works with images. If we don't do this, the image won't show up in the executable.(Pyinstaller)
import sys
import os
import platform

# # For pyinstaller
# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

# For Nuitka 
def resource_path(relative_path):
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)
 


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Genome Uncovered — Bioinformatics for High School")
        # self.state("zoomed")
        if platform.system() == "Linux":
            self.attributes("-fullscreen", True)
        else:
            self.state("zoomed")


        # Canvas
        self.cvs = tk.Canvas(self, bg="black")
        self.cvs.pack(fill="both", expand=True)
        # Bind to the Canvas's Configure event and use event.width/height to get label in the rigth place denoted in resize method
        self.cvs.bind("<Configure>", self.resize)

        # Title
        self.label = tk.Label(
            self.cvs,
            text="Welcome Genome Uncovered!",
            font=("Courier New", 24),
            fg="#00FF9C",
            bg="#0D1117"
        )
        self.label_window = self.cvs.create_window(0, 0, anchor="center", window=self.label)

        # Credit
        self.label2 = tk.Label(
            self.cvs,
            text="© 2026 Ian Vicino. All rights reserved.",
            font=("Courier New", 16),
            fg="#00FF9C",
            bg="#0D1117"
        )
        self.label2_window = self.cvs.create_window(0, 0, anchor="center", window=self.label2)

        # Enter App Button
        self.next_button = tk.Button(
            self,
            text="Start Application",
            font=("Courier New", 20, "bold"),
            bg="#1B4D57",
            fg="white",
            command=self.EnterGame
        )
        self.button_window = self.cvs.create_window(0, 0, window=self.next_button)
        
        # Background Image
        #(Pyinstaller)
        # self.img = Image.open("DNA.png")
        self.img = Image.open(resource_path("DNA.png"))
        self.photo = ImageTk.PhotoImage(self.img)

        self.bg = self.cvs.create_image(0, 0, anchor="nw", image=self.photo)

        # Need to ensure frame transition happens correctly
        self.current_frame = None

    def resize(self, event):

        w = self.cvs.winfo_width()
        h = self.cvs.winfo_height()

        # resize the background image to fill the canvas
        self.cvs.itemconfig(self.bg, image=self.photo)

        self.cvs.coords(self.label_window, w / 2, h * 0.1)
        self.cvs.coords(self.label2_window, w / 2, h * 0.9)
        self.cvs.coords(self.button_window, w / 2, h * 0.5)
        self.cvs.coords(self.bg, 0, 0)

    # How to transition to the next frame (the game)
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def EnterGame(self):
        self.cvs.destroy()  # remove menu
        self.show_frame(twindow) # show next frame (the game)

# Run app
app = Menu()
app.mainloop()