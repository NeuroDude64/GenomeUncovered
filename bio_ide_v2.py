# © 2025 Ian Vicino. All rights reserved.

"""
BioIDE v2 — Levelled Bioinformatics Python Playground for High-School Students
═══════════════════════════════════════════════════════════════════════════════
Six levels of increasing difficulty, 4 problems per level = 24 problems total.
Left panel  : Level sidebar + problem description + DNA data
Right panel : Python code editor → Run → Output console
Features    : progress tracking, hints, expected-output checker, solution reveal
"""

 

import tkinter as tk
from tkinter import ttk, font, scrolledtext, messagebox
import sys, io, traceback, textwrap, json, os

# ════════════════════════════════════════════════════════════════════════════
#  COLOUR PALETTE
# ════════════════════════════════════════════════════════════════════════════
BG_DARK   = "#0d1117"
BG_PANEL  = "#161b22"
BG_EDITOR = "#0d1117"
BG_OUTPUT = "#010409"
BG_SIDE   = "#0d1117"
ACCENT    = "#39d353"
ACCENT2   = "#58a6ff"
RED       = "#f85149"
YELLOW    = "#e3b341"
PURPLE    = "#bc8cff"
ORANGE    = "#ffa657"
TEAL      = "#39c5cf"
BORDER    = "#30363d"
FG_MAIN   = "#e6edf3"
FG_DIM    = "#8b949e"

LEVEL_COLORS = ["#39d353", "#58a6ff", "#e3b341", "#ffa657", "#bc8cff", "#f85149"]
LEVEL_NAMES  = [
    "Level 1 · The Basics",
    "Level 2 · Strings & Strands",
    "Level 3 · Reading the Code",
    "Level 4 · Patterns & Mutations",
    "Level 5 · Data & Analysis",
    "Level 6 · Real-World Genomics",
]
LEVEL_SUBTITLES = [
    "What is DNA? Let's explore it with Python.",
    "Complement, transcription & basic operations.",
    "Codons, proteins & the central dogma.",
    "Motifs, mutations & sequence comparison.",
    "Statistics, GC analysis & multi-sequence work.",
    "Genome assembly, ORF finding & beyond.",
]

# ════════════════════════════════════════════════════════════════════════════
#  CURRICULUM  (6 levels × 4 problems)
# ════════════════════════════════════════════════════════════════════════════
# Each problem dict:
#   title, description, data, starter, expected_output, hints (list of str), solution

CURRICULUM = [

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 1 · The Basics
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "1-1 · Printing a DNA Sequence",
    "description": """\
WELCOME TO Genome Uncovered! 🧬
─────────────────────
DNA (deoxyribonucleic acid) is the molecule that carries
the genetic instructions for all known living things.

A DNA sequence is written as a string of four letters:
  A  Adenine
  T  Thymine
  G  Guanine
  C  Cytosine

TASK
────
The DNA data panel (bottom-left) holds a short DNA sequence.

1. Print the sequence using  print()
2. Print its total length using  len()
3. Print just the FIRST 10 characters (a "slice")

EXPECTED OUTPUT
───────────────
The full sequence
Its length as a number
The first 10 characters

PYTHON TIP
──────────
  seq = DNA_DATA          # grab the sequence
  print(seq)              # print it
  print(len(seq))         # length
  print(seq[:10])         # first 10 characters
""",
    "data": "ATGCTTACGGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCT",
    "starter": """\
# DNA_DATA holds the sequence from the left panel as a string.
# DNA_SEQUENCES holds each line as a list item.

seq = DNA_DATA.strip()

# 1. Print the full sequence
print("Sequence:", seq)

# 2. Print the length — YOUR TURN: fill in the blank
print("Length:", ___)

# 3. Print just the first 10 characters — YOUR TURN
print("First 10:", ___)
""",
    "expected": ["ATGCTTACGGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCT",
                 "43",
                 "ATGCTTACGG"],
    "hints": [
        "Use len(seq) to find the length of any string.",
        "String slicing: seq[start:end] — to get the first 10, use seq[:10]",
        "Replace ___ with the correct expression. For length: len(seq). For slice: seq[:10]",
    ],
    "solution": """\
seq = DNA_DATA.strip()

print("Sequence:", seq)
print("Length:", len(seq))
print("First 10:", seq[:10])
""",
  },

  {
    "title": "1-2 · Counting Nucleotides",
    "description": """\
PROBLEM: Count the Four Bases
──────────────────────────────
Every DNA strand is made of exactly four types of bases.
Knowing how many of each base exists is a fundamental
first step in any genomic analysis.

BACKGROUND
──────────
In Python, strings have a .count() method:
  "AATCG".count("A")  →  2

TASK
────
Count how many times each base (A, T, G, C) appears
in the DNA sequence.

Print the result as:
  A: <count>
  T: <count>
  G: <count>
  C: <count>
  Total: <total>

BIOLOGY CONNECTION
──────────────────
Chargaff's Rule states that in any DNA molecule,
the amount of Adenine equals Thymine, and Guanine
equals Cytosine.  Does your sequence follow this rule?
""",
    "data": "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC",
    "starter": """\
seq = DNA_DATA.strip()

# Count each base using .count()
a = seq.count("A")
t = seq.count(___)   # YOUR TURN
g = ___              # YOUR TURN
c = ___              # YOUR TURN

print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")
print(f"Total: {a + t + g + c}")
""",
    "expected": ["A: 20", "T: 21", "G: 17", "C: 12", "Total: 70"],
    "hints": [
        "seq.count('T') counts how many T's are in the sequence.",
        "For G: g = seq.count('G')   For C: c = seq.count('C')",
        "Chargaff check: A should ≈ T and G should ≈ C. Is that true here?",
    ],
    "solution": """\
seq = DNA_DATA.strip()

a = seq.count("A")
t = seq.count("T")
g = seq.count("G")
c = seq.count("C")

print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")
print(f"Total: {a + t + g + c}")
""",
  },

  {
    "title": "1-3 · GC Content",
    "description": """\
PROBLEM: Calculate GC Content
──────────────────────────────
GC content is the percentage of G and C bases in a
DNA sequence.  It is one of the most widely used
metrics in genomics.

WHY IT MATTERS
──────────────
• G≡C pairs have THREE hydrogen bonds (stronger than A=T's two)
• High GC → more thermally stable DNA
• GC content helps identify species, genes, and genome regions
• Many bacteria have GC content > 60%

TASK
────
Compute and print the GC content as a percentage,
rounded to 2 decimal places.

Formula:
  GC% = (count_G + count_C) / total_length × 100

EXPECTED FORMAT
───────────────
  GC Content: 56.34%
""",
    "data": "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCGCTTCTGCGTTCTGATTTCG",
    "starter": """\
seq = DNA_DATA.strip()

g = seq.count("G")
c = seq.count("C")
total = len(seq)

# Calculate GC content percentage
gc_percent = ___   # YOUR TURN: use the formula above

print(f"G count: {g}")
print(f"C count: {c}")
print(f"Total bases: {total}")
print(f"GC Content: {gc_percent:.2f}%")
""",
    "expected": ["GC Content: 56.34%"],
    "hints": [
        "The formula is: (g + c) / total * 100",
        "gc_percent = (g + c) / total * 100",
        "The :.2f inside f-strings rounds to 2 decimal places automatically.",
    ],
    "solution": """\
seq = DNA_DATA.strip()

g = seq.count("G")
c = seq.count("C")
total = len(seq)

gc_percent = (g + c) / total * 100

print(f"G count: {g}")
print(f"C count: {c}")
print(f"Total bases: {total}")
print(f"GC Content: {gc_percent:.2f}%")
""",
  },

  {
    "title": "1-4 · Reading Frames",
    "description": """\
PROBLEM: Split DNA Into Codons
───────────────────────────────
DNA is read in groups of three bases called CODONS.
Each codon either encodes an amino acid or signals
"stop translating here."

BACKGROUND
──────────
The READING FRAME determines where you start counting.
  Sequence:  A T G C T T A C G G A T
  Frame 1:   ATG | CTT | ACG | GAT
  Frame 2:    TGC | TTA | CGG | AT (incomplete)
  Frame 3:     GCT | TAC | GGA | T  (incomplete)

TASK
────
Using a for-loop with a step of 3, split the DNA sequence
into codons (triplets) starting at position 0.

Print each codon on its own line, numbered 1, 2, 3...
Skip any incomplete codon at the end.

PYTHON TIP
──────────
  for i in range(0, len(seq), 3):
      codon = seq[i:i+3]
""",
    "data": "ATGCTTACGGATCGATCG",
    "starter": """\
seq = DNA_DATA.strip()

print("Reading frame (start position 0):")
codon_num = 1

for i in range(0, len(seq), ___):   # YOUR TURN: step size?
    codon = seq[i:i+3]
    if len(codon) == 3:             # skip incomplete codons
        print(f"  Codon {codon_num}: {codon}")
        codon_num += 1

print(f"Total complete codons: {codon_num - 1}")
""",
    "expected": ["Codon 1: ATG", "Codon 2: CTT", "Codon 3: ACG",
                 "Codon 4: GAT", "Codon 5: CGA", "Codon 6: TCG"],
    "hints": [
        "Codons are 3 bases long, so the step in range() should be 3.",
        "range(0, len(seq), 3) will give you positions 0, 3, 6, 9...",
        "seq[i:i+3] extracts 3 characters starting at position i.",
    ],
    "solution": """\
seq = DNA_DATA.strip()

print("Reading frame (start position 0):")
codon_num = 1

for i in range(0, len(seq), 3):
    codon = seq[i:i+3]
    if len(codon) == 3:
        print(f"  Codon {codon_num}: {codon}")
        codon_num += 1

print(f"Total complete codons: {codon_num - 1}")
""",
  },
],

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 2 · Strings & Strands
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "2-1 · DNA Complement",
    "description": """\
PROBLEM: Find the Complementary Strand
────────────────────────────────────────
DNA is a double helix — two strands wound together.
The bases on opposite strands always pair up:
  A  pairs with  T
  T  pairs with  A
  G  pairs with  C
  C  pairs with  G

TASK
────
Given a DNA sequence, produce its complement by
replacing each base with its pair.

Print the original and complement, aligned.

PYTHON TIP — str.maketrans() and .translate()
─────────────────────────────────────────────
  table = str.maketrans("ATGC", "TACG")
  complement = seq.translate(table)

This is much faster than a for-loop for long sequences!
""",
    "data": "GCATGCATGCATGCATGCAT",
    "starter": """\
seq = DNA_DATA.strip()

# Build a translation table: A↔T, G↔C
table = str.maketrans("ATGC", ___)   # YOUR TURN: what goes here?

complement = seq.translate(table)

print("Original:  ", seq)
print("Complement:", complement)

# Bonus: verify the pairing is correct
for orig, comp in zip(seq[:5], complement[:5]):
    print(f"  {orig} → {comp}")
""",
    "expected": ["Original:   GCATGCATGCATGCATGCAT",
                 "Complement: CGTACGTACGTACGTACGTA"],
    "hints": [
        "str.maketrans maps each character to another. 'ATGC' → 'TACG' means A→T, T→A, G→C, C→G",
        "str.maketrans('ATGC', 'TACG') — the second string must be the same length.",
        "Each position in the first string maps to the same position in the second.",
    ],
    "solution": """\
seq = DNA_DATA.strip()

table = str.maketrans("ATGC", "TACG")
complement = seq.translate(table)

print("Original:  ", seq)
print("Complement:", complement)

for orig, comp in zip(seq[:5], complement[:5]):
    print(f"  {orig} → {comp}")
""",
  },

  {
    "title": "2-2 · Reverse Complement",
    "description": """\
PROBLEM: The Reverse Complement
─────────────────────────────────
DNA strands run in opposite directions — one goes
5'→3' and the other goes 3'→5'.  When biologists
write the "other strand," they write it in the
5'→3' direction, which means:

  Complement the sequence  +  Reverse it

This is called the REVERSE COMPLEMENT and is used
constantly in genomics (primer design, BLAST searches,
gene annotation, and more).

TASK
────
Given the DNA sequence, compute and print:
  1. The complement
  2. The reverse complement
  3. Are they the same? (a palindromic sequence)

PYTHON TIP
──────────
  Reverse a string: seq[::-1]
""",
    "data": "AATTCGCGGCCGCGAATT",
    "starter": """\
seq = DNA_DATA.strip()

table = str.maketrans("ATGC", "TACG")
complement = seq.translate(table)
rev_complement = ___    # YOUR TURN: reverse the complement

print("5'→3' Original:        ", seq)
print("3'→5' Complement:      ", complement)
print("5'→3' Rev. Complement: ", rev_complement)

is_palindrome = (seq == rev_complement)
print(f"\\nPalindromic sequence? {is_palindrome}")
print("(Palindromes are important — restriction enzymes cut them!)")
""",
    "expected": ["Rev. Complement:  AATTCGCGGCCGCGAATT",
                 "Palindromic sequence? True"],
    "hints": [
        "To reverse a string in Python: my_string[::-1]",
        "rev_complement = complement[::-1]",
        "The restriction enzyme EcoRI cuts at GAATTC — a palindrome!",
    ],
    "solution": """\
seq = DNA_DATA.strip()

table = str.maketrans("ATGC", "TACG")
complement = seq.translate(table)
rev_complement = complement[::-1]

print("5'→3' Original:        ", seq)
print("3'→5' Complement:      ", complement)
print("5'→3' Rev. Complement: ", rev_complement)

is_palindrome = (seq == rev_complement)
print(f"\\nPalindromic sequence? {is_palindrome}")
print("(Palindromes are important — restriction enzymes cut them!)")
""",
  },

  {
    "title": "2-3 · Transcription: DNA → mRNA",
    "description": """\
PROBLEM: Transcribe DNA into mRNA
───────────────────────────────────
TRANSCRIPTION is the first step of the central dogma:

  DNA  →  mRNA  →  Protein

During transcription, RNA polymerase reads the template
DNA strand and builds a complementary mRNA strand.

The mRNA sequence matches the CODING strand of DNA,
except Thymine (T) is replaced by Uracil (U):
  DNA coding strand:  5'- A T G C T T -3'
  mRNA:               5'- A U G C U U -3'

TASK
────
Transcribe the DNA coding sequence into mRNA.
Print both sequences, then count how many T→U
substitutions were made.
""",
    "data": "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGT",
    "starter": """\
dna = DNA_DATA.strip()

# Replace every T with U
mrna = dna.replace(___, ___)    # YOUR TURN

t_count = dna.count("T")

print("DNA:  ", dna[:40], "...")
print("mRNA: ", mrna[:40], "...")
print(f"\\nSubstitutions made (T→U): {t_count}")
print(f"mRNA length: {len(mrna)} bases")

# Fun check: are there any T's left in the mRNA?
print(f"Any T in mRNA? {'T' in mrna}")
""",
    "expected": ["Any T in mRNA? False"],
    "hints": [
        "string.replace(old, new) replaces all occurrences.",
        "dna.replace('T', 'U') replaces every T with U.",
        "After replacing, 'T' should not appear anywhere in the mRNA string.",
    ],
    "solution": """\
dna = DNA_DATA.strip()

mrna = dna.replace("T", "U")
t_count = dna.count("T")

print("DNA:  ", dna[:40], "...")
print("mRNA: ", mrna[:40], "...")
print(f"\\nSubstitutions made (T→U): {t_count}")
print(f"mRNA length: {len(mrna)} bases")
print(f"Any T in mRNA? {'T' in mrna}")
""",
  },

  {
    "title": "2-4 · Finding a Start Codon",
    "description": """\
PROBLEM: Locate the Start Codon
─────────────────────────────────
Translation doesn't start at the very beginning of the
mRNA — it starts at the first AUG codon (ATG in DNA),
called the START CODON.

The ribosome scans the mRNA from the 5' end until it
finds AUG, then begins translating.

TASK
────
In the DNA sequence provided:
1. Find the position of the first ATG (start codon)
2. Print everything before it (the 5' UTR)
3. Print the coding sequence (from ATG to the end)
4. Print the position number (1-based)

PYTHON TIP
──────────
  seq.find("ATG")  → returns the index of first match
                     or -1 if not found
""",
    "data": "GGATCGATCGTAGCATGCTTACGGATCGATCGTAG",
    "starter": """\
seq = DNA_DATA.strip()

# Find the first ATG
pos = seq.find(___)    # YOUR TURN

if pos == -1:
    print("No start codon found!")
else:
    utr = seq[:pos]
    coding = seq[pos:]
    print(f"Start codon found at position: {pos + 1} (1-based)")
    print(f"5' UTR (before ATG): '{utr}'  ({len(utr)} bases)")
    print(f"Coding sequence:     '{coding}'")
    print(f"\\nCoding sequence length: {len(coding)} bases")
""",
    "expected": ["Start codon found at position: 14",
                 "Coding sequence:     'ATGCTTACGGATCGATCGTAG'"],
    "hints": [
        "seq.find('ATG') searches for the substring 'ATG' in seq.",
        "The index returned by .find() is 0-based; add 1 for 1-based position.",
        "seq[:pos] gives everything BEFORE position pos; seq[pos:] gives everything FROM pos onward.",
    ],
    "solution": """\
seq = DNA_DATA.strip()

pos = seq.find("ATG")

if pos == -1:
    print("No start codon found!")
else:
    utr = seq[:pos]
    coding = seq[pos:]
    print(f"Start codon found at position: {pos + 1} (1-based)")
    print(f"5' UTR (before ATG): '{utr}'  ({len(utr)} bases)")
    print(f"Coding sequence:     '{coding}'")
    print(f"\\nCoding sequence length: {len(coding)} bases")
""",
  },
],

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 3 · Reading the Code
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "3-1 · The Genetic Code",
    "description": """\
PROBLEM: Translate mRNA → Protein
───────────────────────────────────
TRANSLATION is the second step of the central dogma.
The ribosome reads the mRNA three bases at a time
(codons) and builds a chain of amino acids (a protein).

The GENETIC CODE is a dictionary mapping codons to
amino acids (written in single-letter codes):
  AUG → M (Methionine — the start)
  UAA, UAG, UGA → * (Stop)

TASK
────
Translate the mRNA sequence into a protein string.
• Start at AUG
• Stop (and don't include) the stop codon
• Print the protein sequence and its length

A COMPLETE codon table is provided in the starter code.
""",
    "data": "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA",
    "starter": """\
CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

mrna = DNA_DATA.strip()
protein = []

for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    aa = CODON_TABLE.get(codon, '?')
    if aa == ___:           # YOUR TURN: what stops translation?
        break
    protein.append(aa)

result = ''.join(protein)
print("mRNA:   ", mrna)
print("Protein:", result)
print(f"Length: {len(result)} amino acids")
""",
    "expected": ["Protein: MAMAPRTEINSTRING",
                 "Length: 15 amino acids"],
    "hints": [
        "The stop codons translate to '*' in the table. Use that as your stopping condition.",
        "if aa == '*': break",
        "The expected protein is 'MAMAPRTEINSTRING' — can you see real English words hidden in it? 🧬",
    ],
    "solution": """\
CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

mrna = DNA_DATA.strip()
protein = []

for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    aa = CODON_TABLE.get(codon, '?')
    if aa == '*':
        break
    protein.append(aa)

result = ''.join(protein)
print("mRNA:   ", mrna)
print("Protein:", result)
print(f"Length: {len(result)} amino acids")
""",
  },

  {
    "title": "3-2 · All Three Reading Frames",
    "description": """\
PROBLEM: Translate All 3 Reading Frames
─────────────────────────────────────────
A DNA sequence can be read starting at 3 different
positions — these are the three READING FRAMES.

  Sequence: ATGCTTACG
  Frame 0:  ATG|CTT|ACG  → M L T
  Frame 1:   TGC|TTA|CG  → C L (incomplete)
  Frame 2:    GCT|TAC|G  → A Y (incomplete)

Only one frame usually produces the real protein.
The others often hit stop codons quickly.

TASK
────
Translate the mRNA in all 3 reading frames.
For each frame, print the amino acid sequence
(stop at the first stop codon).
Label which frame produces the LONGEST protein.
""",
    "data": "GCATGCTTACGGATCGATCGTAGCTMRNA\nAUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA",
    "starter": """\
# Use line 2 (the mRNA)
mrna = DNA_SEQUENCES[1]

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(seq):
    protein = []
    for i in range(0, len(seq) - 2, 3):
        aa = CODON_TABLE.get(seq[i:i+3], '?')
        if aa == '*': break
        protein.append(aa)
    return ''.join(protein)

results = []
for frame in range(3):         # frames 0, 1, 2
    subseq = mrna[frame:]      # start reading from offset 'frame'
    protein = translate(___)   # YOUR TURN
    results.append((frame, protein))
    print(f"Frame {frame}: {protein}  ({len(protein)} aa)")

# Find the longest
longest = max(results, key=lambda x: len(x[1]))
print(f"\\nLongest protein in Frame {longest[0]}: {longest[1]}")
""",
    "expected": ["Frame 0: MAMAPRTEINSTRING"],
    "hints": [
        "Pass subseq (the sliced mRNA) into your translate() function.",
        "translate(subseq) — subseq already starts at the right frame offset.",
        "Frame 0 should give the longest protein here.",
    ],
    "solution": """\
mrna = DNA_SEQUENCES[1]

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(seq):
    protein = []
    for i in range(0, len(seq) - 2, 3):
        aa = CODON_TABLE.get(seq[i:i+3], '?')
        if aa == '*': break
        protein.append(aa)
    return ''.join(protein)

results = []
for frame in range(3):
    subseq = mrna[frame:]
    protein = translate(subseq)
    results.append((frame, protein))
    print(f"Frame {frame}: {protein}  ({len(protein)} aa)")

longest = max(results, key=lambda x: len(x[1]))
print(f"\\nLongest protein in Frame {longest[0]}: {longest[1]}")
""",
  },

  {
    "title": "3-3 · Point Mutations",
    "description": """\
PROBLEM: Simulate a Point Mutation
────────────────────────────────────
A POINT MUTATION is a change in a single nucleotide.
These are the most common type of genetic mutation
and can be:
  • SILENT     — amino acid doesn't change
  • MISSENSE   — amino acid changes
  • NONSENSE   — a new stop codon is created

TASK
────
The data has two lines:
  Line 1: Original DNA sequence
  Line 2: Mutated DNA sequence (one base changed)

1. Find the position of the mutation (1-based)
2. Show what changed (e.g. A→G)
3. Transcribe and translate BOTH sequences
4. Determine if the mutation is Silent, Missense, or Nonsense
""",
    "data": "ATGTTCAAAGAGTTCTTCAAGGAGACGGAGCTGGTGGAGACCCTGCACAACTGCTGA\nATGTTCAAAgAGTTCTTCAAGGAGACGGAGCTGGTGGAGACCCTGCACAAGTGCTGA",
    "starter": """\
lines = DNA_SEQUENCES
orig = lines[0].upper()
mutant = lines[1].upper()

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate_dna(seq):
    mrna = seq.replace("T","U")
    protein = []
    for i in range(0, len(mrna)-2, 3):
        aa = CODON_TABLE.get(mrna[i:i+3],'?')
        if aa == '*': break
        protein.append(aa)
    return ''.join(protein)

# Find the mutation position
mut_pos = None
for i, (a, b) in enumerate(zip(orig, mutant)):
    if a != b:
        mut_pos = i
        break

if mut_pos is not None:
    print(f"Mutation at position {mut_pos + 1}: {orig[mut_pos]} → {mutant[mut_pos]}")

p_orig   = translate_dna(orig)
p_mutant = translate_dna(mutant)

print(f"Original protein: {p_orig}")
print(f"Mutant protein:   {p_mutant}")

# YOUR TURN: determine mutation type
if p_orig == p_mutant:
    print("Mutation type: SILENT (same protein)")
elif ___ in p_mutant:         # YOUR TURN: what does nonsense introduce?
    print("Mutation type: NONSENSE (premature stop!)")
else:
    print("Mutation type: MISSENSE (different amino acid)")
""",
    "expected": ["Mutation type: MISSENSE"],
    "hints": [
        "Check if the proteins are the same → Silent",
        "A nonsense mutation creates a premature stop codon — the protein would be shorter.",
        "For nonsense: check if len(p_mutant) < len(p_orig). For the fill-in: '*' in p_mutant won't work since translate stops at '*'. Check lengths instead.",
    ],
    "solution": """\
lines = DNA_SEQUENCES
orig = lines[0].upper()
mutant = lines[1].upper()

CODON_TABLE = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'AUU':'I','AUC':'I','AUA':'I','AUG':'M','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S','CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T','GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'UGU':'C','UGC':'C','UGA':'*','UGG':'W','CGU':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GGU':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate_dna(seq):
    mrna = seq.replace("T","U")
    protein = []
    for i in range(0, len(mrna)-2, 3):
        aa = CODON_TABLE.get(mrna[i:i+3],'?')
        if aa == '*': break
        protein.append(aa)
    return ''.join(protein)

mut_pos = None
for i, (a, b) in enumerate(zip(orig, mutant)):
    if a != b:
        mut_pos = i
        break

if mut_pos is not None:
    print(f"Mutation at position {mut_pos + 1}: {orig[mut_pos]} → {mutant[mut_pos]}")

p_orig   = translate_dna(orig)
p_mutant = translate_dna(mutant)

print(f"Original protein: {p_orig}")
print(f"Mutant protein:   {p_mutant}")

if p_orig == p_mutant:
    print("Mutation type: SILENT (same protein)")
elif len(p_mutant) < len(p_orig):
    print("Mutation type: NONSENSE (premature stop!)")
else:
    print("Mutation type: MISSENSE (different amino acid)")
""",
  },

  {
    "title": "3-4 · Codon Usage Bias",
    "description": """\
PROBLEM: Codon Usage Analysis
───────────────────────────────
Most amino acids can be encoded by MULTIPLE codons.
For example, Leucine (L) can be coded by:
  UUA, UUG, CUU, CUC, CUA, CUG

Organisms tend to PREFER certain synonymous codons
over others — this is called CODON USAGE BIAS and
affects how efficiently genes are translated.

TASK
────
Given an mRNA sequence, count how often each codon
is used.

1. Split into codons (ignore incomplete final codon)
2. Count each unique codon using a dictionary
3. Print the top 5 most used codons
4. Print total unique codons used

PYTHON TIP
──────────
  Use a dict to count: counts[codon] = counts.get(codon, 0) + 1
  Sort: sorted(counts.items(), key=lambda x: x[1], reverse=True)
""",
    "data": "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAAUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAAUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA",
    "starter": """\
mrna = DNA_DATA.strip()

codon_counts = {}
for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    if len(codon) == 3:
        codon_counts[codon] = codon_counts.get(___, 0) + 1   # YOUR TURN

# Sort by frequency descending
sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)

print("Top 5 most-used codons:")
for codon, count in sorted_codons[:5]:
    print(f"  {codon}: {count} times")

print(f"\\nTotal unique codons used: {len(codon_counts)}")
print(f"Total codons counted:     {sum(codon_counts.values())}")
""",
    "expected": ["Total unique codons used: 12"],
    "hints": [
        "codon_counts.get(codon, 0) returns the current count (or 0 if not seen yet), then you add 1.",
        "The key in .get() should be the codon variable: codon_counts.get(codon, 0) + 1",
        "This pattern (get current value or 0, then add 1) is the standard Python way to count things.",
    ],
    "solution": """\
mrna = DNA_DATA.strip()

codon_counts = {}
for i in range(0, len(mrna) - 2, 3):
    codon = mrna[i:i+3]
    if len(codon) == 3:
        codon_counts[codon] = codon_counts.get(codon, 0) + 1

sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)

print("Top 5 most-used codons:")
for codon, count in sorted_codons[:5]:
    print(f"  {codon}: {count} times")

print(f"\\nTotal unique codons used: {len(codon_counts)}")
print(f"Total codons counted:     {sum(codon_counts.values())}")
""",
  },
],

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 4 · Patterns & Mutations
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "4-1 · Motif Finding",
    "description": """\
PROBLEM: Find All Occurrences of a Motif
──────────────────────────────────────────
A MOTIF is a short, recurring nucleotide pattern
that often has biological significance:
  • Promoter sequences (TATAAA — TATA box)
  • Restriction enzyme sites (GAATTC — EcoRI)
  • Transcription factor binding sites

TASK
────
Data has two lines:
  Line 1: A long DNA sequence to search
  Line 2: The motif to find

Find ALL positions where the motif occurs,
including OVERLAPPING matches (overlaps count!).
Report positions in 1-based indexing.

EXAMPLE
───────
Sequence: GATATATGCATATACTT
Motif:    ATAT
Positions: 2 4 10  (overlaps at 2 and 4)
""",
    "data": "AACATGATCAACGAGTTCATGATGATCTCGAAACATGATCAACGAGTTCATGATGATCTCG\nATGAT",
    "starter": """\
seq    = DNA_SEQUENCES[0]
motif  = DNA_SEQUENCES[1]

positions = []
start = 0
while True:
    idx = seq.find(motif, ___)   # YOUR TURN: search from 'start'
    if idx == -1:
        break
    positions.append(idx + 1)    # convert to 1-based
    start = idx + ___            # YOUR TURN: advance by 1 for overlaps

print(f"Sequence length: {len(seq)}")
print(f"Motif: '{motif}' (length {len(motif)})")
print(f"\\nOccurrences found: {len(positions)}")
print(f"Positions (1-based): {positions}")
""",
    "expected": ["Occurrences found: 6"],
    "hints": [
        "seq.find(motif, start) searches starting from index 'start'.",
        "To find overlapping matches, advance by 1 each time: start = idx + 1",
        "If you advance by len(motif) instead, you'll miss overlapping matches.",
    ],
    "solution": """\
seq    = DNA_SEQUENCES[0]
motif  = DNA_SEQUENCES[1]

positions = []
start = 0
while True:
    idx = seq.find(motif, start)
    if idx == -1:
        break
    positions.append(idx + 1)
    start = idx + 1

print(f"Sequence length: {len(seq)}")
print(f"Motif: '{motif}' (length {len(motif)})")
print(f"\\nOccurrences found: {len(positions)}")
print(f"Positions (1-based): {positions}")
""",
  },

  {
    "title": "4-2 · Hamming Distance",
    "description": """\
PROBLEM: Counting Mutations Between Sequences
──────────────────────────────────────────────
The HAMMING DISTANCE between two equal-length strings
is the number of positions where they differ.

In biology this measures:
• The minimum number of point mutations to turn
  one sequence into another
• How similar two gene variants are
• Evolutionary divergence between species

TASK
────
Data has two lines of equal-length DNA sequences.
1. Compute the Hamming distance
2. Print the alignment showing mismatches with '|'
   (matching positions use '.')
3. Print each mismatch position (1-based)

EXAMPLE OUTPUT
──────────────
  Seq1: GAGCCTACTAACGGGAT
  Diff: ...|..|.|.......|
  Seq2: CATCGTAATGACGGCCT
  Hamming distance: 7
""",
    "data": "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT",
    "starter": """\
s1 = DNA_SEQUENCES[0]
s2 = DNA_SEQUENCES[1]

mismatches = []
diff_line = []

for i, (a, b) in enumerate(zip(s1, s2)):
    if a != b:
        mismatches.append(i + 1)
        diff_line.append(___)    # YOUR TURN: marker for mismatch
    else:
        diff_line.append(___)    # YOUR TURN: marker for match

diff_str = ''.join(diff_line)

print(f"Seq1: {s1}")
print(f"Diff: {diff_str}")
print(f"Seq2: {s2}")
print(f"\\nHamming distance: {len(mismatches)}")
print(f"Mismatch positions (1-based): {mismatches}")
""",
    "expected": ["Hamming distance: 7"],
    "hints": [
        "Use '|' for mismatches and '.' for matches.",
        "if a != b: diff_line.append('|')  else: diff_line.append('.')",
        "The Hamming distance is just len(mismatches) since we collected all mismatch positions.",
    ],
    "solution": """\
s1 = DNA_SEQUENCES[0]
s2 = DNA_SEQUENCES[1]

mismatches = []
diff_line = []

for i, (a, b) in enumerate(zip(s1, s2)):
    if a != b:
        mismatches.append(i + 1)
        diff_line.append('|')
    else:
        diff_line.append('.')

diff_str = ''.join(diff_line)

print(f"Seq1: {s1}")
print(f"Diff: {diff_str}")
print(f"Seq2: {s2}")
print(f"\\nHamming distance: {len(mismatches)}")
print(f"Mismatch positions (1-based): {mismatches}")
""",
  },

  {
    "title": "4-3 · Restriction Enzyme Sites",
    "description": """\
PROBLEM: Finding Restriction Enzyme Cut Sites
──────────────────────────────────────────────
RESTRICTION ENZYMES are molecular scissors that
cut DNA at specific recognition sequences.
They are essential tools in genetic engineering.

Common enzymes:
  EcoRI   cuts at  G|AATTC
  BamHI   cuts at  G|GATCC
  HindIII cuts at  A|AGCTT
  NotI    cuts at  GC|GGCCGC

The | shows exactly where the cut happens within
the recognition sequence.

TASK
────
Given a DNA sequence, find all cut sites for three
restriction enzymes. Report the cut position within
the sequence (1-based, at the cut point |).
""",
    "data": "AAGCTTGCATGCCTGCAGGTCGAAGAATTCGATCCGGAATTCAGATCTATTTAAATGAGCTCGCATGCCTGCAG",
    "starter": """\
seq = DNA_DATA.strip()

enzymes = {
    "EcoRI":   ("GAATTC", 1),   # cuts after position 1 within site
    "HindIII": ("AAGCTT", 1),   # cuts after position 1 within site
    "BamHI":   ("GGATCC", 1),
}

for name, (site, cut_offset) in enzymes.items():
    positions = []
    start = 0
    while True:
        idx = seq.find(site, start)
        if idx == -1: break
        cut_pos = idx + cut_offset + 1   # 1-based cut position
        positions.append(cut_pos)
        start = idx + 1

    if positions:
        print(f"{name} ({site}): cuts at positions {positions}")
    else:
        print(f"{name} ({site}): no cut sites found")

# YOUR TURN: How many TOTAL cuts would occur?
all_cuts = ___   # count total from all enzymes above
print(f"\\nTotal restriction cuts: {all_cuts}")
""",
    "expected": ["EcoRI (GAATTC): cuts at positions",
                 "HindIII (AAGCTT): cuts at positions"],
    "hints": [
        "Run the code as-is first to see the outputs, then count total cuts.",
        "Count all positions found across all three enzymes.",
        "EcoRI appears twice, HindIII once → total = 3. Set all_cuts = 3, or better: track counts in a list.",
    ],
    "solution": """\
seq = DNA_DATA.strip()

enzymes = {
    "EcoRI":   ("GAATTC", 1),
    "HindIII": ("AAGCTT", 1),
    "BamHI":   ("GGATCC", 1),
}

total = 0
for name, (site, cut_offset) in enzymes.items():
    positions = []
    start = 0
    while True:
        idx = seq.find(site, start)
        if idx == -1: break
        cut_pos = idx + cut_offset + 1
        positions.append(cut_pos)
        start = idx + 1

    total += len(positions)
    if positions:
        print(f"{name} ({site}): cuts at positions {positions}")
    else:
        print(f"{name} ({site}): no cut sites found")

print(f"\\nTotal restriction cuts: {total}")
""",
  },

  {
    "title": "4-4 · Consensus Sequence",
    "description": """\
PROBLEM: Finding the Consensus Sequence
─────────────────────────────────────────
When you have MULTIPLE aligned DNA sequences (e.g.
from different individuals or species), you can
find the CONSENSUS SEQUENCE — the most common base
at each position.

This is used in:
  • Multiple sequence alignment
  • Finding conserved regions
  • Identifying mutations in a population

TASK
────
Given 5 aligned DNA sequences of equal length,
compute:
1. The consensus sequence (most frequent base at each position)
2. A conservation score per position (fraction of sequences
   that match the consensus, as a percentage)
3. The most conserved and least conserved positions
""",
    "data": "ATGCTTACGG\nATGCTCACGG\nATGCTTACGG\nATGATTACGT\nATGCTTACGG",
    "starter": """\
sequences = DNA_SEQUENCES

# All sequences should be the same length
length = len(sequences[0])
n = len(sequences)

consensus = []
conservation = []

for i in range(length):
    # Get the base at position i for every sequence
    column = [seq[i] for seq in sequences]

    # Find the most common base
    best_base = max("ACGT", key=lambda b: column.count(b))
    consensus.append(best_base)

    # Conservation: fraction that match the best base
    score = column.count(best_base) / n * 100
    conservation.append(score)

cons_str = ''.join(consensus)
print("Consensus: ", cons_str)
print("Per-position conservation (%):")

for i, (base, score) in enumerate(zip(cons_str, conservation)):
    bar = "█" * int(score // 10)
    print(f"  Pos {i+1:2d}: {base}  {score:5.1f}%  {bar}")

best_pos  = conservation.index(max(conservation)) + 1
worst_pos = conservation.index(min(conservation)) + 1
print(f"\\nMost conserved position:  {best_pos}  ({max(conservation):.1f}%)")
print(f"Least conserved position: {worst_pos}  ({min(conservation):.1f}%)")
""",
    "expected": ["Consensus:  ATGCTTACGG",
                 "Most conserved position"],
    "hints": [
        "This starter code is nearly complete — try running it first!",
        "column.count(b) counts how many times base b appears at that column.",
        "max('ACGT', key=lambda b: column.count(b)) finds the most frequent base.",
    ],
    "solution": """\
sequences = DNA_SEQUENCES

length = len(sequences[0])
n = len(sequences)

consensus = []
conservation = []

for i in range(length):
    column = [seq[i] for seq in sequences]
    best_base = max("ACGT", key=lambda b: column.count(b))
    consensus.append(best_base)
    score = column.count(best_base) / n * 100
    conservation.append(score)

cons_str = ''.join(consensus)
print("Consensus: ", cons_str)
print("Per-position conservation (%):")

for i, (base, score) in enumerate(zip(cons_str, conservation)):
    bar = "█" * int(score // 10)
    print(f"  Pos {i+1:2d}: {base}  {score:5.1f}%  {bar}")

best_pos  = conservation.index(max(conservation)) + 1
worst_pos = conservation.index(min(conservation)) + 1
print(f"\\nMost conserved position:  {best_pos}  ({max(conservation):.1f}%)")
print(f"Least conserved position: {worst_pos}  ({min(conservation):.1f}%)")
""",
  },
],

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 5 · Data & Analysis
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "5-1 · GC Content Sliding Window",
    "description": """\
PROBLEM: GC Content Across a Genome
─────────────────────────────────────
Real genomes don't have uniform GC content — it
varies across the chromosome in regions called
GC-rich islands and AT-rich regions.

CpG ISLANDS are GC-rich regions near gene promoters
and are important in gene regulation and cancer biology.

TASK
────
Use a SLIDING WINDOW to compute GC content across
the sequence. A sliding window moves along the
sequence one base at a time, computing a value
over each window of fixed size.

Window size: 10 bases
Step size:   5 bases

Print the GC% for each window, then identify which
windows are potential CpG islands (GC > 60%).
""",
    "data": "ATATATATATAGCGCGCGCGCGATATATATATAGCGCGCGCGCGATATATATATAGCGCGCGCGCGATATAT",
    "starter": """\
seq = DNA_DATA.strip()
window_size = 10
step = 5

print(f"Sliding window GC content (window={window_size}, step={step})")
print(f"{'Window':>8}  {'Sequence':>12}  {'GC%':>6}  {'CpG?':>5}")
print("-" * 45)

cpg_windows = []

for start in range(0, len(seq) - window_size + 1, step):
    end = start + window_size
    window = seq[start:end]

    gc = (window.count('G') + window.count('C')) / window_size * 100
    is_cpg = gc > ___           # YOUR TURN: threshold for CpG island

    label = "★ CpG" if is_cpg else ""
    if is_cpg:
        cpg_windows.append(start + 1)

    print(f"{start+1:>5}-{end:>3}  {window:>12}  {gc:>5.1f}%  {label}")

print(f"\\nPotential CpG island windows starting at: {cpg_windows}")
print(f"Total CpG-rich windows: {len(cpg_windows)}")
""",
    "expected": ["CpG island windows", "Total CpG-rich windows"],
    "hints": [
        "CpG islands are defined as GC content > 60%.",
        "is_cpg = gc > 60",
        "The sequence was designed to alternate AT-rich and GC-rich regions — you should see the pattern!",
    ],
    "solution": """\
seq = DNA_DATA.strip()
window_size = 10
step = 5

print(f"Sliding window GC content (window={window_size}, step={step})")
print(f"{'Window':>8}  {'Sequence':>12}  {'GC%':>6}  {'CpG?':>5}")
print("-" * 45)

cpg_windows = []

for start in range(0, len(seq) - window_size + 1, step):
    end = start + window_size
    window = seq[start:end]
    gc = (window.count('G') + window.count('C')) / window_size * 100
    is_cpg = gc > 60

    label = "★ CpG" if is_cpg else ""
    if is_cpg:
        cpg_windows.append(start + 1)

    print(f"{start+1:>5}-{end:>3}  {window:>12}  {gc:>5.1f}%  {label}")

print(f"\\nPotential CpG island windows starting at: {cpg_windows}")
print(f"Total CpG-rich windows: {len(cpg_windows)}")
""",
  },

  {
    "title": "5-2 · Open Reading Frame Finder",
    "description": """\
PROBLEM: Find All Open Reading Frames (ORFs)
──────────────────────────────────────────────
An OPEN READING FRAME (ORF) is a sequence of DNA that
begins with a start codon (ATG) and ends with a stop
codon (TAA, TAG, or TGA) with no stop codons in between.

Real genes are found by scanning all 6 possible reading
frames (3 forward + 3 reverse complement).

TASK
────
Search the FORWARD strand only (3 frames) for all ORFs.
For each ORF found:
  • Print its frame, start position, stop position
  • Print its length in codons
  • Translate and print the protein sequence

Only report ORFs of at least 3 codons (>= 9 bases).
""",
    "data": "ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGACGCGTAAAATGGTGCATCTGACTCCTGAGGAGAAGTGA",
    "starter": """\
seq = DNA_DATA.strip()
STOP_CODONS = {"TAA","TAG","TGA"}
CODON_TABLE = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

orfs_found = 0

for frame in range(3):
    i = frame
    while i < len(seq) - 2:
        codon = seq[i:i+3]
        if codon == "ATG":       # found a start codon
            # scan forward for a stop codon
            protein = []
            j = i
            while j < len(seq) - 2:
                c = seq[j:j+3]
                if c in STOP_CODONS:
                    # ORF ends here
                    if len(protein) >= 3:    # at least 3 amino acids
                        orfs_found += 1
                        prot_str = ''.join(protein)
                        print(f"ORF {orfs_found}: Frame {frame}, pos {i+1}-{j+3}")
                        print(f"  Length: {len(protein)} codons")
                        print(f"  Protein: {prot_str}")
                    break
                aa = CODON_TABLE.get(c, '?')
                protein.append(aa)
                j += 3
        i += ___    # YOUR TURN: how far to advance each step?

print(f"\\nTotal ORFs found: {orfs_found}")
""",
    "expected": ["Total ORFs found: 2"],
    "hints": [
        "In the outer loop, advance one codon at a time to not skip any potential start codons in this frame.",
        "i += 3 — advance by one codon (3 bases) in the outer scanning loop.",
        "The inner loop (j) already handles the translation; the outer loop (i) scans for new ATG starts.",
    ],
    "solution": """\
seq = DNA_DATA.strip()
STOP_CODONS = {"TAA","TAG","TGA"}
CODON_TABLE = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

orfs_found = 0

for frame in range(3):
    i = frame
    while i < len(seq) - 2:
        codon = seq[i:i+3]
        if codon == "ATG":
            protein = []
            j = i
            while j < len(seq) - 2:
                c = seq[j:j+3]
                if c in STOP_CODONS:
                    if len(protein) >= 3:
                        orfs_found += 1
                        prot_str = ''.join(protein)
                        print(f"ORF {orfs_found}: Frame {frame}, pos {i+1}-{j+3}")
                        print(f"  Length: {len(protein)} codons")
                        print(f"  Protein: {prot_str}")
                    break
                aa = CODON_TABLE.get(c, '?')
                protein.append(aa)
                j += 3
        i += 3

print(f"\\nTotal ORFs found: {orfs_found}")
""",
  },

  {
    "title": "5-3 · Sequence Similarity Score",
    "description": """\
PROBLEM: Pairwise Sequence Similarity
───────────────────────────────────────
Before powerful tools like BLAST existed, biologists
compared sequences using SIMILARITY SCORES.

A simple scoring scheme:
  Match:    +2  (same base)
  Mismatch: -1  (different base)
  Gap:      -2  (missing base, shown as '-')

TASK
────
Given two aligned sequences (same length, gaps shown as '-'),
compute the alignment score and percent identity.

Data has 3 lines:
  Line 1: Sequence 1 (with gaps)
  Line 2: Sequence 2 (with gaps)
  Line 3: A reference label

Print the alignment with a match/mismatch line,
the total score, and the percent identity.
""",
    "data": "ATGCTTACGGATCGATCG\nATGCT-ACGGTTCGATCG\nHuman vs Chimp BRCA1 fragment",
    "starter": """\
s1    = DNA_SEQUENCES[0]
s2    = DNA_SEQUENCES[1]
label = DNA_SEQUENCES[2]

MATCH    =  2
MISMATCH = -1
GAP      = -2

score = 0
matches = 0
align_line = []

for a, b in zip(s1, s2):
    if a == '-' or b == '-':
        score += GAP
        align_line.append(' ')
    elif a == b:
        score += ___        # YOUR TURN
        matches += 1
        align_line.append('|')
    else:
        score += ___        # YOUR TURN
        align_line.append('.')

non_gap = sum(1 for a,b in zip(s1,s2) if a != '-' and b != '-')
pct_id  = matches / non_gap * 100 if non_gap else 0

print(f"Alignment: {label}")
print(f"Seq1: {s1}")
print(f"      {''.join(align_line)}")
print(f"Seq2: {s2}")
print(f"\\nMatches:         {matches} / {non_gap} aligned positions")
print(f"Percent identity: {pct_id:.1f}%")
print(f"Alignment score: {score}")
""",
    "expected": ["Percent identity: 88.2%",
                 "Alignment score:"],
    "hints": [
        "On a match: score += MATCH (which is +2)",
        "On a mismatch: score += MISMATCH (which is -1)",
        "Use the variable names MATCH and MISMATCH that are already defined.",
    ],
    "solution": """\
s1    = DNA_SEQUENCES[0]
s2    = DNA_SEQUENCES[1]
label = DNA_SEQUENCES[2]

MATCH    =  2
MISMATCH = -1
GAP      = -2

score = 0
matches = 0
align_line = []

for a, b in zip(s1, s2):
    if a == '-' or b == '-':
        score += GAP
        align_line.append(' ')
    elif a == b:
        score += MATCH
        matches += 1
        align_line.append('|')
    else:
        score += MISMATCH
        align_line.append('.')

non_gap = sum(1 for a,b in zip(s1,s2) if a != '-' and b != '-')
pct_id  = matches / non_gap * 100 if non_gap else 0

print(f"Alignment: {label}")
print(f"Seq1: {s1}")
print(f"      {''.join(align_line)}")
print(f"Seq2: {s2}")
print(f"\\nMatches:         {matches} / {non_gap} aligned positions")
print(f"Percent identity: {pct_id:.1f}%")
print(f"Alignment score: {score}")
""",
  },

  {
    "title": "5-4 · DNA Repeat Finder",
    "description": """\
PROBLEM: Finding Tandem Repeats
─────────────────────────────────
TANDEM REPEATS are sequences where a short motif
is repeated consecutively:
  e.g.  ATGATGATGATG  = (ATG) × 4

They are important in:
  • DNA fingerprinting / forensics (STRs)
  • Genetic diseases (Huntington's = CAG repeats)
  • Chromosome structure (telomeres = TTAGGG repeats)

TASK
────
Given a DNA sequence, find all tandem repeats
of motifs between 2 and 6 bases long.

For each repeat unit found, report:
  • The motif
  • How many times it repeats
  • The start and end position
  • Only report runs of 3+ repeats
""",
    "data": "ATGATGATGATGCCCCCCCTAGCATCATCATCATCATCATGCGCGCGCGCGCGATGATG",
    "starter": """\
seq = DNA_DATA.strip()

print(f"Searching for tandem repeats in {len(seq)}-base sequence\\n")

found = []
for motif_len in range(2, 7):           # motif lengths 2-6
    i = 0
    while i <= len(seq) - motif_len:
        motif = seq[i:i+motif_len]
        count = 1
        j = i + motif_len
        while j + motif_len <= len(seq) and seq[j:j+motif_len] == motif:
            count += 1
            j += motif_len

        if count >= ___:                 # YOUR TURN: minimum repeat count
            end_pos = i + motif_len * count
            found.append((motif, count, i+1, end_pos))
            i = end_pos                  # skip past this repeat
        else:
            i += 1

# Deduplicate (remove sub-repeats)
found.sort(key=lambda x: -x[1])
seen = set()
for motif, count, start, end in found:
    key = (start, end)
    if key not in seen:
        seen.add(key)
        print(f"  Motif: {motif:6s}  ×{count}  pos {start}-{end}  "
              f"({motif * count})")

print(f"\\nTotal tandem repeats found: {len(seen)}")
""",
    "expected": ["Total tandem repeats found"],
    "hints": [
        "We only want runs of 3 or more repeats to avoid noise.",
        "count >= 3",
        "The sequence contains ATG×4, C×7, CATCAT×3, CGCG×3 — see if you can find them all!",
    ],
    "solution": """\
seq = DNA_DATA.strip()

print(f"Searching for tandem repeats in {len(seq)}-base sequence\\n")

found = []
for motif_len in range(2, 7):
    i = 0
    while i <= len(seq) - motif_len:
        motif = seq[i:i+motif_len]
        count = 1
        j = i + motif_len
        while j + motif_len <= len(seq) and seq[j:j+motif_len] == motif:
            count += 1
            j += motif_len

        if count >= 3:
            end_pos = i + motif_len * count
            found.append((motif, count, i+1, end_pos))
            i = end_pos
        else:
            i += 1

found.sort(key=lambda x: -x[1])
seen = set()
for motif, count, start, end in found:
    key = (start, end)
    if key not in seen:
        seen.add(key)
        print(f"  Motif: {motif:6s}  ×{count}  pos {start}-{end}  ({motif * count})")

print(f"\\nTotal tandem repeats found: {len(seen)}")
""",
  },
],

# ─────────────────────────────────────────────────────────────────────────────
# LEVEL 6 · Real-World Genomics
# ─────────────────────────────────────────────────────────────────────────────
[
  {
    "title": "6-1 · Parse a FASTA File",
    "description": """\
PROBLEM: Reading the FASTA Format
───────────────────────────────────
FASTA is the universal file format for biological
sequences.  Every genome database uses it.

Format:
  >SequenceID description
  ATGCTTACGGATCGATCG...
  ATCGATCGATCG...

  >AnotherSequence description
  GCTAGCTAGCTA...

The ">" line is the header; all following lines
(until the next ">") are the sequence.

TASK
────
Parse the multi-FASTA data and:
1. Count how many sequences there are
2. Print each sequence's ID and length
3. Find and print the longest sequence
4. Compute GC content for each sequence
""",
    "data": ">seq1 Homo sapiens BRCA1 fragment\nATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAG\n>seq2 Pan troglodytes BRCA1 fragment\nATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAGTGTCATTAATGCTATGCAGAAAATCTTAG\n>seq3 Mus musculus Brca1 fragment\nATGGATCTATCTGCTCTTCGTGTTGAAGAAGTGCAGATGTCATTAACGCTATGCAGAAAATCTTAGA",
    "starter": """\
raw = DNA_DATA

# Parse FASTA format
sequences = {}
current_id = None
current_seq = []

for line in raw.strip().split('\\n'):
    if line.startswith('>'):
        if current_id:
            sequences[current_id] = ''.join(current_seq)
        header = line[1:].split()
        current_id = header[0]       # sequence ID
        current_seq = []
    else:
        current_seq.append(___)      # YOUR TURN: add sequence line

# Don't forget the last sequence!
if current_id:
    sequences[current_id] = ''.join(current_seq)

print(f"Sequences found: {len(sequences)}\\n")

for seq_id, seq in sequences.items():
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    print(f"  {seq_id}: {len(seq)} bp  |  GC: {gc:.1f}%")
    print(f"    {seq[:30]}...")

longest_id = max(sequences, key=lambda k: len(sequences[k]))
print(f"\\nLongest sequence: {longest_id} ({len(sequences[longest_id])} bp)")
""",
    "expected": ["Sequences found: 3",
                 "Longest sequence:"],
    "hints": [
        "You need to add the current line to current_seq.",
        "current_seq.append(line.strip()) — strip removes whitespace/newlines.",
        "The final sequence isn't saved inside the loop, so the 'if current_id' after the loop handles that.",
    ],
    "solution": """\
raw = DNA_DATA

sequences = {}
current_id = None
current_seq = []

for line in raw.strip().split('\\n'):
    if line.startswith('>'):
        if current_id:
            sequences[current_id] = ''.join(current_seq)
        header = line[1:].split()
        current_id = header[0]
        current_seq = []
    else:
        current_seq.append(line.strip())

if current_id:
    sequences[current_id] = ''.join(current_seq)

print(f"Sequences found: {len(sequences)}\\n")

for seq_id, seq in sequences.items():
    gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
    print(f"  {seq_id}: {len(seq)} bp  |  GC: {gc:.1f}%")
    print(f"    {seq[:30]}...")

longest_id = max(sequences, key=lambda k: len(sequences[k]))
print(f"\\nLongest sequence: {longest_id} ({len(sequences[longest_id])} bp)")
""",
  },

  {
    "title": "6-2 · Genome Assembly (De Bruijn)",
    "description": """\
PROBLEM: Assembling Reads with De Bruijn Graphs
─────────────────────────────────────────────────
Modern sequencing machines don't read whole genomes
at once — they produce millions of short READS.
Genome assemblers stitch them back together.

One approach: DE BRUIJN GRAPHS
  1. Break each read into k-mers (substrings of length k)
  2. Build a graph where edges represent k-mers
  3. Find a path through all edges (Eulerian path)

SIMPLIFIED VERSION
──────────────────
Given a set of short DNA reads, reconstruct the
original sequence by finding overlaps.

TASK
────
Given reads of length 5, reconstruct the original
sequence using overlap-based assembly (each read
overlaps the next by k-1 bases).

Reads are in correct order for this exercise.
Print the assembled sequence.
""",
    "data": "ATGCA\nTGCAT\nGCATG\nCATGC\nATGCT\nTGCTA\nGCTAG\nCTAGC\nTAGCT",
    "starter": """\
reads = DNA_SEQUENCES
k = len(reads[0])
overlap = k - 1

print(f"Assembling {len(reads)} reads of length {k}")
print(f"Overlap size: {overlap} bases\\n")

# Start with the first read
assembly = reads[0]

for i in range(1, len(reads)):
    prev = reads[i-1]
    curr = reads[i]

    # The overlap is the last (k-1) bases of prev == first (k-1) bases of curr
    prev_suffix = prev[-overlap:]
    curr_prefix = curr[:overlap]

    if prev_suffix == curr_prefix:
        # Add only the new (non-overlapping) part
        new_base = curr[___:]    # YOUR TURN: which part is new?
        assembly += new_base
        print(f"  Read {i+1}: ...{prev_suffix}|{curr[overlap:]}  ✓")
    else:
        print(f"  Read {i+1}: OVERLAP MISMATCH! {prev_suffix} ≠ {curr_prefix}")

print(f"\\nAssembled sequence ({len(assembly)} bp):")
print(assembly)
""",
    "expected": ["Assembled sequence"],
    "hints": [
        "The 'new' part of each read is everything AFTER the overlap.",
        "curr[overlap:] gives the new bases — overlap is k-1 = 4.",
        "So new_base = curr[overlap:] which means curr[4:] — just the last 1 new base per read.",
    ],
    "solution": """\
reads = DNA_SEQUENCES
k = len(reads[0])
overlap = k - 1

print(f"Assembling {len(reads)} reads of length {k}")
print(f"Overlap size: {overlap} bases\\n")

assembly = reads[0]

for i in range(1, len(reads)):
    prev = reads[i-1]
    curr = reads[i]

    prev_suffix = prev[-overlap:]
    curr_prefix = curr[:overlap]

    if prev_suffix == curr_prefix:
        new_base = curr[overlap:]
        assembly += new_base
        print(f"  Read {i+1}: ...{prev_suffix}|{curr[overlap:]}  ✓")
    else:
        print(f"  Read {i+1}: OVERLAP MISMATCH! {prev_suffix} ≠ {curr_prefix}")

print(f"\\nAssembled sequence ({len(assembly)} bp):")
print(assembly)
""",
  },

  {
    "title": "6-3 · Phylogenetic Distance Matrix",
    "description": """\
PROBLEM: Building a Distance Matrix
─────────────────────────────────────
Phylogenetics studies the evolutionary relationships
between species.  One approach compares DNA sequences
to estimate how diverged they are.

A DISTANCE MATRIX shows the similarity (or difference)
between every pair of sequences — it is the foundation
of tree-building algorithms like UPGMA and Neighbor-Joining.

TASK
────
Given 4 species with aligned sequences of the same gene,
build a pairwise distance matrix.

Distance = Hamming distance / sequence length (normalized)

Print:
1. A formatted distance matrix
2. Which two species are most closely related
3. Which two are most distantly related

This is similar to what MEGA and other phylogenetics
software do with real genomic data!
""",
    "data": "Human    ATGCTTACGGATCGATCGATGCTTACGG\nChimp    ATGCTTACGGATCGATCGATGCTTACGG\nGorilla  ATGCTTACGGTTCGCTCGATGCTTACGT\nMouse    ATGATCACGGTTCGATCGATGTTTACGG",
    "starter": """\
lines = DNA_SEQUENCES
species = []
seqs    = []

for line in lines:
    parts = line.split()
    species.append(parts[0])
    seqs.append(parts[1])

n = len(species)

def hamming_dist(s1, s2):
    return sum(a != b for a, b in zip(s1, s2)) / len(s1)

# Build distance matrix
matrix = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            matrix[i][j] = hamming_dist(seqs[i], seqs[j])

# Print matrix
col_w = 10
print("Distance Matrix (normalized Hamming)\\n")
header = " " * 10 + "".join(f"{s:>{col_w}}" for s in species)
print(header)

for i, row_name in enumerate(species):
    row = f"{row_name:<10}" + "".join(f"{matrix[i][j]:>{col_w}.4f}" for j in range(n))
    print(row)

# Find closest and most distant pairs
closest  = (None, None, 1.0)
farthest = (None, None, 0.0)

for i in range(n):
    for j in range(i+1, n):
        d = matrix[i][j]
        if d < closest[2]:
            closest = (species[i], species[j], d)
        if d > farthest[___]:    # YOUR TURN: which index?
            farthest = (species[i], species[j], d)

print(f"\\nClosest pair:   {closest[0]} & {closest[1]}  (distance {closest[2]:.4f})")
print(f"Farthest pair:  {farthest[0]} & {farthest[1]}  (distance {farthest[2]:.4f})")
""",
    "expected": ["Distance Matrix",
                 "Closest pair:",
                 "Farthest pair:"],
    "hints": [
        "The tuple is (species1, species2, distance). Distance is at index [2].",
        "farthest[2] is the current maximum distance.",
        "if d > farthest[2]: farthest = (species[i], species[j], d)",
    ],
    "solution": """\
lines = DNA_SEQUENCES
species = []
seqs    = []

for line in lines:
    parts = line.split()
    species.append(parts[0])
    seqs.append(parts[1])

n = len(species)

def hamming_dist(s1, s2):
    return sum(a != b for a, b in zip(s1, s2)) / len(s1)

matrix = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            matrix[i][j] = hamming_dist(seqs[i], seqs[j])

col_w = 10
print("Distance Matrix (normalized Hamming)\\n")
header = " " * 10 + "".join(f"{s:>{col_w}}" for s in species)
print(header)

for i, row_name in enumerate(species):
    row = f"{row_name:<10}" + "".join(f"{matrix[i][j]:>{col_w}.4f}" for j in range(n))
    print(row)

closest  = (None, None, 1.0)
farthest = (None, None, 0.0)

for i in range(n):
    for j in range(i+1, n):
        d = matrix[i][j]
        if d < closest[2]:
            closest = (species[i], species[j], d)
        if d > farthest[2]:
            farthest = (species[i], species[j], d)

print(f"\\nClosest pair:   {closest[0]} & {closest[1]}  (distance {closest[2]:.4f})")
print(f"Farthest pair:  {farthest[0]} & {farthest[1]}  (distance {farthest[2]:.4f})")
""",
  },

  {
    "title": "6-4 · Sickle Cell Disease — A Real Mutation",
    "description": """\
CAPSTONE PROBLEM: Sickle Cell Disease 🩸
─────────────────────────────────────────
This is a real genetic variant that affects millions
of people worldwide.

SICKLE CELL DISEASE is caused by a single point
mutation in the HBB gene (beta-globin):
  Normal:  GAG  →  Glutamic acid (E)
  Mutant:  GTG  →  Valine (V)

This single amino acid change (E6V) causes hemoglobin
to polymerise under low oxygen conditions, deforming
red blood cells into a sickle shape.

TASK — Put it ALL together!
────────────────────────────
You have the first 90 bases of the normal and sickle
HBB coding sequences.

1. Find the mutation position
2. Determine which codon changed and what amino acids differ
3. Translate BOTH proteins and compare them
4. Annotate the difference with an arrow at the changed position

This is exactly the kind of analysis done when
sequencing patient genomes for genetic counselling.
""",
    "data": "ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG\nATGGTGCATCTGACTCCTGTGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAG",
    "starter": """\
normal = DNA_SEQUENCES[0]
sickle = DNA_SEQUENCES[1]

CODON_TABLE = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(seq):
    p = []
    for i in range(0, len(seq)-2, 3):
        aa = CODON_TABLE.get(seq[i:i+3], '?')
        if aa == '*': break
        p.append(aa)
    return ''.join(p)

# 1. Find mutation position
mut_positions = [i+1 for i,(a,b) in enumerate(zip(normal,sickle)) if a!=b]
print(f"Mutation(s) at position(s): {mut_positions}")

# 2. Identify changed codon
for pos in mut_positions:
    idx = pos - 1
    codon_num = idx // 3        # which codon (0-indexed)
    codon_start = codon_num * 3
    norm_codon = normal[codon_start:codon_start+3]
    sick_codon = sickle[codon_start:codon_start+3]
    norm_aa = CODON_TABLE.get(norm_codon, '?')
    sick_aa = CODON_TABLE.get(sick_codon, '?')
    print(f"\\nCodon {codon_num+1}:")
    print(f"  Normal:  {norm_codon} → {norm_aa}")
    print(f"  Sickle:  {sick_codon} → {sick_aa}")

# 3. Translate both
p_normal = translate(normal)
p_sickle = translate(sickle)

print(f"\\nNormal protein: {p_normal}")
print(f"Sickle protein: {p_sickle}")

# 4. YOUR TURN: annotate the difference
# Print a line under the protein showing where they differ
diff_marker = []
for a, b in zip(p_normal, p_sickle):
    if a != b:
        diff_marker.append(___)   # YOUR TURN: marker for difference
    else:
        diff_marker.append(' ')

print(f"Difference:     {''.join(diff_marker)}")
print(f"\\n★ The E→V change at position 6 is the cause of Sickle Cell Disease.")
print(f"  One base (A→T), one amino acid change, life-altering consequences.")
""",
    "expected": ["Normal protein: MVHLTPEEKSAVTALWGKVNVDEVGGEALG",
                 "Sickle protein: MVHLTPVEKSAVTALWGKVNVDEVGGEALG",
                 "E→V change at position 6"],
    "hints": [
        "The diff_marker should visually point to the changed amino acid.",
        "Use '^' as the difference marker: diff_marker.append('^')",
        "You should see exactly one '^' at position 6 of the protein — the E6V mutation!",
    ],
    "solution": """\
normal = DNA_SEQUENCES[0]
sickle = DNA_SEQUENCES[1]

CODON_TABLE = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
    'ATT':'I','ATC':'I','ATA':'I','ATG':'M','GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S','CCT':'P','CCC':'P','CCA':'P','CCG':'P',
    'ACT':'T','ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A','GCA':'A','GCG':'A',
    'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'AAT':'N','AAC':'N','AAA':'K','AAG':'K','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
    'TGT':'C','TGC':'C','TGA':'*','TGG':'W','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
    'AGT':'S','AGC':'S','AGA':'R','AGG':'R','GGT':'G','GGC':'G','GGA':'G','GGG':'G',
}

def translate(seq):
    p = []
    for i in range(0, len(seq)-2, 3):
        aa = CODON_TABLE.get(seq[i:i+3], '?')
        if aa == '*': break
        p.append(aa)
    return ''.join(p)

mut_positions = [i+1 for i,(a,b) in enumerate(zip(normal,sickle)) if a!=b]
print(f"Mutation(s) at position(s): {mut_positions}")

for pos in mut_positions:
    idx = pos - 1
    codon_num = idx // 3
    codon_start = codon_num * 3
    norm_codon = normal[codon_start:codon_start+3]
    sick_codon = sickle[codon_start:codon_start+3]
    norm_aa = CODON_TABLE.get(norm_codon, '?')
    sick_aa = CODON_TABLE.get(sick_codon, '?')
    print(f"\\nCodon {codon_num+1}:")
    print(f"  Normal:  {norm_codon} → {norm_aa}")
    print(f"  Sickle:  {sick_codon} → {sick_aa}")

p_normal = translate(normal)
p_sickle = translate(sickle)

print(f"\\nNormal protein: {p_normal}")
print(f"Sickle protein: {p_sickle}")

diff_marker = ['^' if a != b else ' ' for a, b in zip(p_normal, p_sickle)]
print(f"Difference:     {''.join(diff_marker)}")
print(f"\\n★ The E→V change at position 6 is the cause of Sickle Cell Disease.")
print(f"  One base (A→T), one amino acid change, life-altering consequences.")
""",
  },
],

]  # end CURRICULUM


# TODO: 
# Add Title screen and credits - DONE
# Add a screen showing the core concepts learned in the application - DONE
# Add a connection to the Biology curriculum - DONE
# I need another screen after the core concepts to reveal what students are about to see - DONE

# Add this stuff in the documentation/README:
# Add a link to the textbook I used to learn Python < Add it after I show how to use the app
# Add a video, or document showing how the app is used for teachers and students

# Add a "for teachers" section with tips on how to use it in the classroom



# ════════════════════════════════════════════════════════════════════════════
#  PROGRESS SAVE/LOAD  (simple JSON file next to the script)
# ════════════════════════════════════════════════════════════════════════════
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bioide_progress.json")

def load_progress():
    try:
        with open(SAVE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}

def save_progress(data):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

# ════════════════════════════════════════════════════════════════════════════
#  MAIN APPLICATION
# ════════════════════════════════════════════════════════════════════════════
# class BioIDE(tk.Tk): # we use tk.Frame instead of tk.Tk to allow embedding in other contexts (e.g. Jupyter)
class BioIDE(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # # Not needed as we're using tk.Frame, but if this were tk.Tk, we'd set up the window here:
        # self.title("BioIDE v2 — Bioinformatics for High School")
        # self.configure(bg=BG_DARK)
        # self.geometry("1400x860")
        # self.minsize(1000, 680)
        # self.state("zoomed")

        self._level     = 0
        self._prob_idx  = 0
        self._hint_idx  = 0
        self._progress  = load_progress()   # {"L-P": True/False}
        self._code_cache = {}               # save per-problem edits
        self._code_cache["0-0"] = CURRICULUM[0][0]["starter"] # it just pre-seeds the cache with the correct starter so there's never an empty string to accidentally load.

        self._build_fonts()
        self._build_ui()
        self._select_level(0)
        self._load_problem(0, 0)

    # ── fonts ──────────────────────────────────────────────────────────────
    def _build_fonts(self):
        self.font_mono   = font.Font(family="Courier", size=11)
        self.font_mono_b = font.Font(family="Courier", size=11, weight="bold")
        self.font_ui     = font.Font(family="Helvetica", size=10)
        self.font_ui_b   = font.Font(family="Helvetica", size=10, weight="bold")
        self.font_title  = font.Font(family="Helvetica", size=13, weight="bold")
        self.font_small  = font.Font(family="Helvetica", size=9)
        self.font_lvl    = font.Font(family="Helvetica", size=11, weight="bold")
        self.font_prob   = font.Font(family="Helvetica", size=10)

    # ── top bar ────────────────────────────────────────────────────────────
    def _build_topbar(self):
        bar = tk.Frame(self, bg=BG_PANEL, height=48)
        bar.pack(fill="x", side="top")
        bar.pack_propagate(False)

        tk.Label(bar, text="🧬  Genome Uncovered", bg=BG_PANEL, fg=ACCENT,
                 font=self.font_title).pack(side="left", padx=16, pady=10)

        self._top_subtitle = tk.Label(bar, text="", bg=BG_PANEL,
                                      fg=FG_DIM, font=self.font_ui)
        self._top_subtitle.pack(side="left", padx=4)

        # total progress
        total = sum(6 * [4])  # 24
        done  = sum(1 for v in self._progress.values() if v)
        self._prog_lbl = tk.Label(bar, text=f"Progress: {done}/{total}",
                                  bg=BG_PANEL, fg=FG_DIM, font=self.font_ui)
        self._prog_lbl.pack(side="right", padx=16)

        tk.Frame(self, bg=BORDER, height=1).pack(fill="x", side="top")

    # ── full UI ────────────────────────────────────────────────────────────
    def _build_ui(self):
        self._build_topbar()

        # ── outer horizontal split: sidebar | content ─────────────────────
        outer = tk.PanedWindow(self, orient="horizontal",
                               bg=BORDER, sashwidth=4, sashrelief="flat", bd=0)
        outer.pack(fill="both", expand=True)

        # ── SIDEBAR ───────────────────────────────────────────────────────
        self._sidebar = tk.Frame(outer, bg=BG_SIDE, width=220)
        outer.add(self._sidebar, minsize=180, width=220)
        self._build_sidebar()

        # ── MAIN CONTENT ──────────────────────────────────────────────────
        content = tk.Frame(outer, bg=BG_DARK)
        outer.add(content, minsize=700)

        # inner split: left (problem) | right (editor)
        inner = tk.PanedWindow(content, orient="horizontal",
                               bg=BORDER, sashwidth=4, sashrelief="flat", bd=0)
        inner.pack(fill="both", expand=True)

        # LEFT problem panel
        left = tk.Frame(inner, bg=BG_PANEL)
        inner.add(left, minsize=320, width=480)
        self._build_left(left)

        # RIGHT editor panel
        right = tk.Frame(inner, bg=BG_DARK)
        inner.add(right, minsize=320)
        self._build_right(right)

    # ── sidebar ────────────────────────────────────────────────────────────
    def _build_sidebar(self):
        tk.Label(self._sidebar, text="  LEVELS", bg=BG_SIDE,
                 fg=FG_DIM, font=self.font_small,
                 anchor="w").pack(fill="x", pady=(10,4))

        self._level_frames = []
        self._prob_buttons = [[] for _ in range(6)]

        for lvl in range(6):
            color = LEVEL_COLORS[lvl]

            # Level header button
            lhdr = tk.Frame(self._sidebar, bg=BG_SIDE)
            lhdr.pack(fill="x", padx=4, pady=(4,0))

            btn = tk.Button(lhdr, text=f"  {LEVEL_NAMES[lvl]}",
                            bg=BG_SIDE, fg=color,
                            font=self.font_lvl,
                            relief="flat", bd=0,
                            anchor="w", padx=6, pady=6,
                            cursor="hand2",
                            activebackground=BORDER,
                            activeforeground=color,
                            command=lambda l=lvl: self._select_level(l))
            btn.pack(fill="x")

            # Problem sub-buttons
            prob_frame = tk.Frame(self._sidebar, bg=BG_SIDE)
            prob_frame.pack(fill="x", padx=4)
            self._level_frames.append(prob_frame)

            for pi in range(4):
                p = CURRICULUM[lvl][pi]
                key = f"{lvl}-{pi}"
                done = self._progress.get(key, False)
                marker = "✓ " if done else "○ "
                short = p["title"].split("·",1)[1].strip() if "·" in p["title"] else p["title"]
                short = short[:26] + "…" if len(short) > 26 else short

                pb = tk.Button(prob_frame,
                               text=f"   {marker}{short}",
                               bg=BG_SIDE, fg=FG_DIM if not done else ACCENT,
                               font=self.font_prob,
                               relief="flat", bd=0,
                               anchor="w", padx=4, pady=3,
                               cursor="hand2",
                               activebackground=BORDER,
                               activeforeground=FG_MAIN,
                               command=lambda l=lvl, p=pi: self._load_problem(l, p))
                pb.pack(fill="x")
                self._prob_buttons[lvl].append(pb)

            prob_frame.pack_forget()   # start collapsed

        # spacer + credit
        tk.Frame(self._sidebar, bg=BG_SIDE).pack(fill="both", expand=True)
        tk.Label(self._sidebar, text="Genome Uncovered", bg=BG_SIDE,
                 fg=BORDER, font=self.font_small).pack(pady=8)

    # ── left panel (problem) ───────────────────────────────────────────────
    def _build_left(self, parent):
        # problem title bar
        self._prob_title_lbl = tk.Label(parent, text="",
                                         bg=BG_PANEL, fg=FG_MAIN,
                                         font=self.font_title,
                                         anchor="w", padx=12, pady=8)
        self._prob_title_lbl.pack(fill="x")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        hdr = tk.Frame(parent, bg=BG_PANEL)
        hdr.pack(fill="x")
        tk.Label(hdr, text="📋  Problem Description", bg=BG_PANEL,
                 fg=ACCENT2, font=self.font_ui_b, pady=5, padx=10).pack(side="left")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        self._desc_text = scrolledtext.ScrolledText(
            parent, bg=BG_PANEL, fg=FG_MAIN, font=self.font_mono,
            bd=0, relief="flat", wrap="word", state="disabled",
            insertbackground=ACCENT, selectbackground="#264f78")
        self._desc_text.pack(fill="both", expand=True)
        self._style_scroll(self._desc_text)

        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")
        hdr2 = tk.Frame(parent, bg=BG_PANEL)
        hdr2.pack(fill="x")
        tk.Label(hdr2, text="🧬  DNA / Sequence Data", bg=BG_PANEL,
                 fg=YELLOW, font=self.font_ui_b, pady=5, padx=10).pack(side="left")
        tk.Label(hdr2, text="(editable — try your own sequences!)",
                 bg=BG_PANEL, fg=FG_DIM, font=self.font_small).pack(side="left")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        self._data_text = scrolledtext.ScrolledText(
            parent, bg=BG_EDITOR, fg=YELLOW, font=self.font_mono,
            bd=0, relief="flat", wrap="word", height=7,
            insertbackground=ACCENT, selectbackground="#264f78")
        self._data_text.pack(fill="x")
        self._style_scroll(self._data_text)

    # ── right panel (editor + output) ─────────────────────────────────────
    def _build_right(self, parent):
        # toolbar
        toolbar = tk.Frame(parent, bg=BG_PANEL)
        toolbar.pack(fill="x")

        self._run_btn = tk.Button(toolbar, text="▶  Run",
            bg=ACCENT, fg=BG_DARK, font=self.font_ui_b,
            relief="flat", bd=0, padx=18, pady=7,
            activebackground="#2ea043", activeforeground=BG_DARK,
            cursor="hand2", command=self._run_code)
        self._run_btn.pack(side="left", padx=10, pady=6)

        self._hint_btn = tk.Button(toolbar, text="💡  Hint",
            bg=BG_PANEL, fg=YELLOW, font=self.font_ui,
            relief="flat", bd=0, padx=12, pady=7,
            activebackground=BORDER, activeforeground=YELLOW,
            cursor="hand2", command=self._show_hint)
        self._hint_btn.pack(side="left", padx=4, pady=6)

        self._soln_btn = tk.Button(toolbar, text="🔑  Solution",
            bg=BG_PANEL, fg=PURPLE, font=self.font_ui,
            relief="flat", bd=0, padx=12, pady=7,
            activebackground=BORDER, activeforeground=PURPLE,
            cursor="hand2", command=self._show_solution)
        self._soln_btn.pack(side="left", padx=4, pady=6)

        self._reset_btn = tk.Button(toolbar, text="↩  Reset",
            bg=BG_PANEL, fg=FG_DIM, font=self.font_ui,
            relief="flat", bd=0, padx=12, pady=7,
            activebackground=BORDER, activeforeground=FG_MAIN,
            cursor="hand2", command=self._reset_code)
        self._reset_btn.pack(side="left", padx=4, pady=6)

        self._check_btn = tk.Button(toolbar, text="✓  Check Output",
            bg=BG_PANEL, fg=TEAL, font=self.font_ui,
            relief="flat", bd=0, padx=12, pady=7,
            activebackground=BORDER, activeforeground=TEAL,
            cursor="hand2", command=self._check_output)
        self._check_btn.pack(side="left", padx=4, pady=6)

        self._status_lbl = tk.Label(toolbar, text="", bg=BG_PANEL,
                                    font=self.font_small)
        self._status_lbl.pack(side="right", padx=12)
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        hdr = tk.Frame(parent, bg=BG_PANEL)
        hdr.pack(fill="x")
        tk.Label(hdr, text="✏️  Python Editor", bg=BG_PANEL,
                 fg=ACCENT, font=self.font_ui_b, pady=5, padx=10).pack(side="left")
        self._hint_counter = tk.Label(hdr, text="", bg=BG_PANEL,
                                       fg=YELLOW, font=self.font_small)
        self._hint_counter.pack(side="right", padx=10)
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        self._code_text = scrolledtext.ScrolledText(
            parent, bg=BG_EDITOR, fg=FG_MAIN, font=self.font_mono,
            bd=0, relief="flat", wrap="none",
            insertbackground=ACCENT, selectbackground="#264f78",
            tabs=("4c",))
        self._code_text.pack(fill="both", expand=True)
        self._style_scroll(self._code_text)
        self._code_text.bind("<Tab>", self._on_tab)

        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")
        hdr2 = tk.Frame(parent, bg=BG_PANEL)
        hdr2.pack(fill="x")
        tk.Label(hdr2, text="⚡  Output", bg=BG_PANEL,
                 fg=RED, font=self.font_ui_b, pady=5, padx=10).pack(side="left")
        tk.Frame(parent, bg=BORDER, height=1).pack(fill="x")

        self._out_text = scrolledtext.ScrolledText(
            parent, bg=BG_OUTPUT, fg=ACCENT, font=self.font_mono,
            bd=0, relief="flat", wrap="word", height=10, state="disabled",
            insertbackground=ACCENT, selectbackground="#264f78")
        self._out_text.pack(fill="both", expand=False)
        self._style_scroll(self._out_text)

        self._out_text.tag_config("error",  foreground=RED)
        self._out_text.tag_config("ok",     foreground=ACCENT)
        self._out_text.tag_config("info",   foreground=FG_DIM)
        self._out_text.tag_config("hint",   foreground=YELLOW)
        self._out_text.tag_config("pass",   foreground=ACCENT)
        self._out_text.tag_config("fail",   foreground=RED)
        self._out_text.tag_config("soln",   foreground=PURPLE)

    # ── helpers ────────────────────────────────────────────────────────────
    def _style_scroll(self, w):
        w.vbar.config(bg=BG_PANEL, troughcolor=BG_DARK,
                      activebackground=BORDER, width=8, relief="flat")

    def _on_tab(self, event):
        self._code_text.insert(tk.INSERT, "    ")
        return "break"

    # ── level / problem selection ──────────────────────────────────────────
    def _select_level(self, lvl):
        for l in range(6):
            if l == lvl:
                self._level_frames[l].pack(fill="x", padx=4)
            else:
                self._level_frames[l].pack_forget()

    def _load_problem(self, lvl, pi):
        # cache current editor contents for the previous problem
        cache_key = f"{self._level}-{self._prob_idx}"
        current_code = self._code_text.get("1.0", tk.END).strip()
        if current_code:                                          # ← only cache if not empty
            self._code_cache[cache_key] = current_code

        self._level    = lvl
        self._prob_idx = pi
        self._hint_idx = 0

        p = CURRICULUM[lvl][pi]
        color = LEVEL_COLORS[lvl]

        # title bar
        self._prob_title_lbl.config(text=f"  {p['title']}", fg=color)
        self._top_subtitle.config(text=LEVEL_NAMES[lvl] + "  —  " + LEVEL_SUBTITLES[lvl])

        # description
        self._desc_text.config(state="normal")
        self._desc_text.delete("1.0", tk.END)
        self._desc_text.insert("1.0", p["description"])
        self._desc_text.config(state="disabled")

        # data
        self._data_text.delete("1.0", tk.END)
        self._data_text.insert("1.0", p["data"])

        # code — restore cache or use starter
        new_key = f"{lvl}-{pi}"
        code = self._code_cache.get(new_key, p["starter"])
        self._code_text.delete("1.0", tk.END)
        self._code_text.insert("1.0", code)

        # highlight active problem button
        for l in range(6):
            for pi2, pb in enumerate(self._prob_buttons[l]):
                key = f"{l}-{pi2}"
                done = self._progress.get(key, False)
                is_active = (l == lvl and pi2 == pi)
                pb.config(
                    fg=ACCENT if done else (FG_MAIN if is_active else FG_DIM),
                    bg="#1c2128" if is_active else BG_SIDE)

        hints = p.get("hints", [])
        self._hint_counter.config(text=f"Hints available: {len(hints)}")

        self._clear_output()
        self._write_output(f"# {p['title']} loaded.\n# Press ▶ Run to execute your code.\n", "info")
        self._select_level(lvl)

    # ── run code ──────────────────────────────────────────────────────────
    def _run_code(self):
        code     = self._code_text.get("1.0", tk.END)
        raw_data = self._data_text.get("1.0", tk.END).strip()
        sequences = [l for l in raw_data.splitlines() if l.strip()]

        self._clear_output()
        self._write_output("▶  Running…\n", "info")

        old_out, old_err = sys.stdout, sys.stderr
        buf = io.StringIO()
        sys.stdout = sys.stderr = buf

        inject = {"DNA_DATA": raw_data, "DNA_SEQUENCES": sequences}

        try:
            exec(compile(code, "<BioIDE>", "exec"), inject)
            out = buf.getvalue()
            self._write_output(out if out else "(no output)\n", "ok")
            self._set_status("✔  OK", ACCENT)
        except Exception:
            out = buf.getvalue()
            if out: self._write_output(out, "ok")
            self._write_output(traceback.format_exc(), "error")
            self._set_status("✘  Error", RED)
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    # ── check output ──────────────────────────────────────────────────────
    def _check_output(self):
        """Run the code and check if expected strings appear in output."""
        code     = self._code_text.get("1.0", tk.END)
        raw_data = self._data_text.get("1.0", tk.END).strip()
        sequences = [l for l in raw_data.splitlines() if l.strip()]
        p = CURRICULUM[self._level][self._prob_idx]
        expected = p.get("expected", [])

        if not expected:
            self._write_output("\n(No automated check for this problem.)\n", "info")
            return

        self._clear_output()
        self._write_output("▶  Running + checking…\n\n", "info")

        old_out, old_err = sys.stdout, sys.stderr
        buf = io.StringIO()
        sys.stdout = sys.stderr = buf

        inject = {"DNA_DATA": raw_data, "DNA_SEQUENCES": sequences}
        passed = 0

        try:
            exec(compile(code, "<BioIDE>", "exec"), inject)
            out = buf.getvalue()
            self._write_output(out + "\n", "ok")

            self._write_output("─" * 40 + "\n", "info")
            self._write_output("Output checks:\n", "info")

            for check in expected:
                if check.lower() in out.lower():
                    self._write_output(f"  ✓  Found: \"{check}\"\n", "pass")
                    passed += 1
                else:
                    self._write_output(f"  ✗  Missing: \"{check}\"\n", "fail")

            if passed == len(expected):
                self._write_output(f"\n🎉  All {passed} checks passed!\n", "pass")
                self._set_status("✔  Correct!", ACCENT)
                self._mark_complete()
            else:
                self._write_output(f"\n{passed}/{len(expected)} checks passed.\n", "fail")
                self._set_status(f"  {passed}/{len(expected)} checks", YELLOW)

        except Exception:
            out = buf.getvalue()
            if out: self._write_output(out, "ok")
            self._write_output(traceback.format_exc(), "error")
            self._set_status("✘  Error", RED)
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def _mark_complete(self):
        key = f"{self._level}-{self._prob_idx}"
        if not self._progress.get(key):
            self._progress[key] = True
            save_progress(self._progress)
            # refresh sidebar button
            pb = self._prob_buttons[self._level][self._prob_idx]
            p = CURRICULUM[self._level][self._prob_idx]
            short = p["title"].split("·",1)[1].strip() if "·" in p["title"] else p["title"]
            short = short[:26] + "…" if len(short) > 26 else short
            pb.config(text=f"   ✓ {short}", fg=ACCENT)
            # update progress label
            done = sum(1 for v in self._progress.values() if v)
            self._prog_lbl.config(text=f"Progress: {done}/24")

    # ── hints ──────────────────────────────────────────────────────────────
    def _show_hint(self):
        p = CURRICULUM[self._level][self._prob_idx]
        hints = p.get("hints", [])
        if not hints:
            self._write_output("\n💡  No hints for this problem.\n", "hint")
            return
        if self._hint_idx >= len(hints):
            self._write_output("\n💡  No more hints — try the Solution button!\n", "hint")
            return
        self._write_output(f"\n💡  Hint {self._hint_idx+1}/{len(hints)}:\n    {hints[self._hint_idx]}\n", "hint")
        self._hint_idx += 1
        remaining = len(hints) - self._hint_idx
        self._hint_counter.config(text=f"Hints remaining: {remaining}")

    # ── solution ──────────────────────────────────────────────────────────
    def _show_solution(self):
        p = CURRICULUM[self._level][self._prob_idx]
        if messagebox.askyesno("Show Solution?",
                               "Are you sure you want to see the solution?\n"
                               "Try the hints first — you learn more by trying!",
                               icon="warning"):
            self._code_text.delete("1.0", tk.END)
            self._code_text.insert("1.0", p["solution"])
            self._write_output("\n🔑  Solution loaded into editor. Run it to see the output!\n", "soln")
            self._set_status("Solution shown", PURPLE)

    # ── reset / clear ──────────────────────────────────────────────────────
    def _reset_code(self):
        p = CURRICULUM[self._level][self._prob_idx]
        self._code_text.delete("1.0", tk.END)
        self._code_text.insert("1.0", p["starter"])
        cache_key = f"{self._level}-{self._prob_idx}"
        if cache_key in self._code_cache:
            del self._code_cache[cache_key]
        self._clear_output()
        self._write_output("# Code reset to starter template.\n", "info")

    def _clear_output(self):
        self._out_text.config(state="normal")
        self._out_text.delete("1.0", tk.END)
        self._out_text.config(state="disabled")
        self._set_status("", FG_DIM)

    def _write_output(self, text, tag="ok"):
        self._out_text.config(state="normal")
        self._out_text.insert(tk.END, text, tag)
        self._out_text.see(tk.END)
        self._out_text.config(state="disabled")

    def _set_status(self, text, color):
        self._status_lbl.config(text=text, fg=color, bg=BG_PANEL)


# ════════════════════════════════════════════════════════════════════════════
# if __name__ == "__main__":
#     app = BioIDE()
#     app.mainloop()
