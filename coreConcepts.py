# © 2026 Ian Vicino. All rights reserved.

import tkinter as tk
from PIL import Image, ImageTk

from bio_ide_v2 import BioIDE
from Preview import preview

 
CORE_CONCEPTS = [
    {
        "topic": "DNA Structure & Composition",
        "levels": "Levels 1–2",
        "summary": "Work with the four nucleotide bases (A, T, G, C), discover Chargaff's Rule experimentally by counting bases, and learn why GC content matters through hydrogen bonding strength.",
        "curriculum": "Molecular Biology Unit, Chapter 1 foundations",
    },
    
    {
        "topic": "DNA Replication & Complementarity",
        "levels": "Level 2",
        "summary": "Compute complement and reverse complement strands. Reinforces how DNA unzips, how each strand serves as a template, and the concept of antiparallel 5'→3' directionality.",
        "curriculum": "DNA Replication unit; base-pairing rules",
    },
    {
        "topic": "The Central Dogma",
        "levels": "Levels 2–3",
        "summary": "Execute each step of DNA → mRNA → Protein in code. Transcription (T→U) and translation (codons → amino acids) become concrete processes rather than abstract diagrams.",
        "curriculum": "AP Biology Unit 6 — Gene Expression & Regulation",
    },
    {
        "topic": "The Genetic Code & Protein Synthesis",
        "levels": "Level 3",
        "summary": "Read codons across all three reading frames using the codon table. Shows concretely why a single insertion mutation shifts the entire reading frame and disrupts the protein.",
        "curriculum": "AP Biology Unit 6; translation & the codon table",
    },
    {
        "topic": "Mutations",
        "levels": "Levels 3–4",
        "summary": "Compare two sequences to identify silent, missense, and nonsense mutations and see their protein-level consequences. Directly sets up the sickle cell capstone in Level 6.",
        "curriculum": "Mutations unit; AP Biology Unit 6",
    },
    {
        "topic": "Gene Regulation & Promoters",
        "levels": "Level 4",
        "summary": "Search for transcription factor binding sites and promoter sequences like the TATA box. Students learn why short motifs have enormous biological significance.",
        "curriculum": "Gene regulation; AP Biology Unit 6",
    },
    {
        "topic": "Biotechnology & Genetic Engineering",
        "levels": "Level 4",
        "summary": "Find EcoRI and HindIII restriction enzyme cut sites computationally — the same concept behind gel electrophoresis labs. Mirrors exactly what researchers do before designing an experiment.",
        "curriculum": "Biotechnology unit; restriction enzymes & gel electrophoresis",
    },
    {
        "topic": "Heredity & Genetic Variation",
        "levels": "Level 4",
        "summary": "Use Hamming distance and consensus sequences to quantify genetic variation within a population. Connects to Hardy-Weinberg equilibrium and allele frequency concepts.",
        "curriculum": "Genetics & heredity; population genetics",
    },
    {
        "topic": "Epigenetics & Gene Expression",
        "levels": "Level 5",
        "summary": "Detect CpG islands using a sliding window. Introduces DNA methylation and gene silencing — one of the most exciting modern additions to high school biology.",
        "curriculum": "Epigenetics; gene expression regulation; cancer biology",
    },
    {
        "topic": "Genomics & Bioinformatics",
        "levels": "Level 6",
        "summary": "Parse FASTA format, find open reading frames, and assemble reads — the actual tools professional scientists use. Connects to the Human Genome Project and personalized medicine.",
        "curriculum": "Genomics; bioinformatics; biotechnology applications",
    },
    {
        "topic": "Evolution & Phylogenetics",
        "levels": "Level 6",
        "summary": "Build a pairwise distance matrix comparing Human, Chimp, Gorilla, and Mouse sequences. A computational version of the cladograms students draw by hand, making the molecular clock tangible.",
        "curriculum": "Evolution unit; cladistics; molecular clock",
    },
    {
        "topic": "Human Genetics & Disease",
        "levels": "Level 6",
        "summary": "Apply every skill to the real sickle cell disease mutation (E6V in HBB). Covers Mendelian genetics, codominance, natural selection in malaria regions, and the ethics of genetic screening.",
        "curriculum": "Human genetics; genetic diseases; AP Biology Unit 5",
    },
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



class coreConcepts(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Canvas - Make background black and fill whole screen
        self.cvs = tk.Canvas(self, bg="black")
        self.cvs.pack(fill="both", expand=True)
        # Bind to the Canvas's Configure event and use event.width/height to get label in the rigth place denoted in resize method
        self.cvs.bind("<Configure>", self.resize)

        # Background Image
        #(Pyinstaller)
        # self.img = Image.open("flyingDNA.png")
        self.img = Image.open(resource_path("flyingDNA.png"))
        self.photo = ImageTk.PhotoImage(self.img)

        self.bg = self.cvs.create_image(0, 0, anchor="nw", image=self.photo)

        # Need to ensure frame transition happens correctly
        self.current_frame = None

        # Title
        self.label = tk.Label(
            self.cvs,
            text="Core Concepts you will learn",
            font=("Courier New", 24),
            fg="#00FF9C",
            bg="#0D1117"
        )
        self.label_window = self.cvs.create_window(0, 0, anchor="center", window=self.label)

        # Concepts List
        self.label2 = tk.Label(
            self.cvs,
            text="\n".join(
                (lambda c: f"{c['levels']:12} {c['topic']}")(concept)
                for concept in CORE_CONCEPTS
            ),
            font=("Courier New", 18),
            fg="#00FF9C",
            bg="#0D1117",
            justify="left"
        )
        self.label2_window = self.cvs.create_window(0, 0, anchor="center", window=self.label2)

        self.button = tk.Button(
            self,
            text="Continue",
            font=("Courier New", 20, "bold"),
            bg="#1B4D57",
            fg="white",
            command=self.continueG
        )
        self.button_window = self.cvs.create_window(0, 0, anchor="center", window=self.button)


    def resize(self, event):

        w = self.cvs.winfo_width()
        h = self.cvs.winfo_height()

        # # resize the background image to fill the canvas
        # self.cvs.itemconfig(self.bg, image=self.photo)

        self.cvs.coords(self.label_window, w / 2, h * 0.1)
        self.cvs.coords(self.label2_window, w / 2, h * 0.5)
        self.cvs.coords(self.button_window, w / 2, h * 0.9)
        self.cvs.coords(self.bg, 0, 0)

    # How to transition to the next frame (the game)
    def show_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def continueG(self):
        self.cvs.destroy()  # remove menu
        self.show_frame(preview) # show next frame (the game)