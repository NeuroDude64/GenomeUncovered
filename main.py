
# © 2026 Ian Vicino. All rights reserved.

import tkinter as tk
from menu import Menu
# from bio_ide_v2 import BioIDE

# ════════════════════════════════════════════════════════════════════════════
#  COLOUR PALETTE
# ════════════════════════════════════════════════════════════════════════════
BG_DARK   = "#0d1117"

 
class App1(tk.Tk):
    def __init__(self):
        super().__init__()
       
        self.current_frame = None
        self.show_frame(Menu)

    def show_frame(self, frame_class):
        # Destroy old frame
        if self.current_frame is not None:
            self.current_frame.destroy()

        # Create new frame
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)



# Not needed:
 # self.title("Genome Uncovered — Bioinformatics for High School")
        # self.configure(bg=BG_DARK)
        # self.geometry("1400x860")
        # self.minsize(1000, 680)
        # self.state("zoomed")