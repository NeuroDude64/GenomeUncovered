# © 2026 Ian Vicino. All rights reserved.

import tkinter as tk
from PIL import Image, ImageTk

from bio_ide_v2 import BioIDE
 
students = [
    "Students:",
    "\n===CODED BEFORE:===",
    "If you have some programming experience, you might find this program familiar.",
    "\n===NEVER CODED BEFORE:===",
    "If you have never coded before, the program may seem intimidating at first.",
    "To the right is a preview of the program you will be using.",
    "It looks like a Python IDE (Interactive Development Environment).",
    "Don't worry — it will guide you step by step!"
]

# Used because of how pyinstaller works with images. If we don't do this, the image won't show up in the executable.(Pyinstaller)
import sys
import os

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




class preview(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#0D1117")

        self.parent = parent
        self.current_frame = None

        # =========================
        # GRID STRUCTURE (3 rows)
        # =========================
        self.rowconfigure(0, weight=1)  # title
        self.rowconfigure(1, weight=3)  # content
        self.rowconfigure(2, weight=1)  # button
        self.columnconfigure(0, weight=1)

        # =========================
        # TITLE
        # =========================
        title = tk.Label(
            self,
            text="Preview",
            font=("Courier New", 24, "bold"),
            fg="#00FF9C",
            bg="#0D1117"
        )
        title.grid(row=0, column=0, pady=10)

        # =========================
        # MAIN CONTAINER (LEFT / RIGHT)
        # =========================
        container = tk.Frame(self, bg="#0D1117")
        container.grid(row=1, column=0, sticky="nsew", padx=20)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(0, weight=1)

        # ----- LEFT (TEXT) -----
        left_frame = tk.Frame(container, bg="#0D1117")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10)

        text_label = tk.Label(
            left_frame,
            text="\n\n".join(students),
            font=("Courier New", 12),
            fg="#00FF9C",
            bg="#0D1117",
            justify="left",
            wraplength=400
        )
        text_label.pack(anchor="n", pady=10)

        # ----- RIGHT (IMAGE) -----
        right_frame = tk.Frame(container, bg="#0D1117")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10)

        #(Pyinstaller)
        # img = Image.open("BioInform.png")
        img = Image.open(resource_path("BioInform.png"))
        img = img.resize((700, 400), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(right_frame, image=self.photo, bg="#0D1117")
        img_label.pack(expand=True)

        # =========================
        # BUTTON (BOTTOM)
        # =========================
        button = tk.Button(
            self,
            text="Continue",
            font=("Courier New", 18, "bold"),
            bg="#1B4D57",
            fg="white",
            command=self.continueG
        )
        button.grid(row=2, column=0, pady=20)

    # =========================
    # FRAME SWITCHING
    # =========================
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame_class(self.parent)
        self.current_frame.pack(fill="both", expand=True)

    def continueG(self):
        self.destroy()
        self.show_frame(BioIDE)