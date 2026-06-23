# GenomeUncovered
This is a program I developed to introduce high school students, and some exceptional middle school students, to bioinformatics. 

By running through this application you can not only learn what bioinformatics is, but flex your critical thinking by solving some bioinformatics problems without needing to know how to code. 

Why did I add this program to GitHub? 
I am hoping you might improve this software and use it to teach students about bioinformatics. By adding my code here I have more potential of my application, modified or not, getting into the hands of a high school student and introducing them to bioinformatics. That would be a win for me. 

main.py is the starting code to start the application
menu.py is the starting window of the application
coreConcepts.py is a window showing the biology concepts that will be discussed during the main application
Preview.py is a preview of what you will see in the main window of the application
bio_ide_v2.py is the main application window. It looks and acts like a python IDE that is run locally on your computer

If you are a teacher or student acessing this application here is the ReadMe for the application:
_________________________________________
Genome Uncovered
Bioinformatics for High School
________________________________________
Table of Contents
1.	Overview
2.	Students
3.	Biology Teachers
4.	A note from the Developer
5.	Computer Science Teachers
6.	Feedback
7.	Core Concepts Learned through this Application

Overview
Genome Uncovered is designed to bridge the gap between biology concepts taught in the classroom and the types of data analysis performed in real research labs. It introduces students to how scientists work with biological data in college-level courses and professional settings.
By the end of the program, students will be able to:
•	Analyze genomic data 
•	Understand transcription and translation 
•	Explore basic proteomic data 
More importantly, students will see how these skills connect to real-world applications, such as developing treatments and cures for a wide range of diseases.
________________________________________
For Students
This software is designed to be intuitive and beginner-friendly. As you progress through the levels, you will learn both key biology concepts and how to use Python to analyze biological data.
You do not need prior coding experience. The program guides you step-by-step using a structured, fill-in-the-blank approach.
To help you get started:
•	A video tutorial is included with the software 
•	A recommended Python textbook is linked here: https://automatetheboringstuff.com/ 
•	Many free online resources are available if you want to explore further
Follow your teacher’s guidance as you work through the program. If you have ideas for improvements or features you’d like to see, your feedback is welcome—this project is continually evolving to better support your learning.
________________________________________
For Biology Teachers
This software allows students to use Python to analyze genetic data, without requiring you to have prior programming experience.
To get started:
•	Watch the included introductory video 
•	Try a few levels yourself to become familiar with the interface 
How to Use in the Classroom
Genome Uncovered is designed to complement your existing curriculum. You can integrate it into lessons on:
•	DNA structure 
•	The genome 
•	Transcription and translation 
•	The central dogma 
Each level introduces a new biological concept while gradually increasing in difficulty. The software can be used:
•	As a supplement to reinforce lessons 
•	As a primer before introducing new topics 
•	As part of a larger unit on bioinformatics 
A Note from the Developer
This is an early version of the software, and your feedback is extremely valuable. The goal is to make this a meaningful tool that helps students connect classroom biology to modern computational biology and research practices.
________________________________________
For Computer Science Teachers
Students with programming experience may find the coding aspects approachable, but they may need support understanding the biological context.
To ensure success:
•	Collaborate with biology teachers when possible 
•	Ensure students understand key concepts such as: 
o	DNA structure 
o	Transcription (DNA → RNA) 
o	Translation (RNA → protein) 
o	Differences between DNA, RNA, and protein sequences 
Once the biological foundation is in place, students will be able to apply their coding skills to meaningful genetic analysis problems.
While this software is not primarily designed to teach Python, it provides a strong example of how programming can be applied in real-world scientific contexts. Many students may progress quickly through the levels and benefit from the interdisciplinary challenge.
________________________________________
Collaboration Encouraged
This project is inherently interdisciplinary. Collaboration between biology and computer science educators will provide the most meaningful experience for students.
________________________________________
Feedback
This software is a work in progress, and you are among the first educators and students to use it. Your feedback, suggestions, and ideas are greatly appreciated and will help improve the experience for future users.
Core Concepts Learned in Application:
DNA Structure & Composition Levels 1-2 build this foundation directly. Students work with the four nucleotide bases (A, T, G, C), discover Chargaff's Rule experimentally by counting bases, and learn why GC content matters through the lens of hydrogen bonding strength. These are usually Chapter 1 concepts in any molecular biology unit.
________________________________________
The Central Dogma This is the backbone of Levels 2 and 3 — DNA → mRNA → Protein. Students don't just memorize the arrows, they execute each step in code. Transcription (replacing T with U) and translation (reading codons against a codon table) become concrete processes rather than abstract diagrams. Most state standards and AP Biology Unit 6 center heavily on this.
________________________________________
DNA Replication & Complementarity The complement and reverse complement problems (Level 2) connect directly to how DNA unzips and how each strand serves as a template. The reverse complement also introduces the concept of antiparallel strands and 5'→3' directionality, which trips up a lot of students when taught abstractly.
________________________________________
The Genetic Code & Protein Synthesis Level 3 dives into codons, reading frames, and the codon table — all standard curriculum content. The three reading frames problem is particularly powerful because it shows students why a single insertion mutation is so catastrophic (it shifts the entire reading frame).
________________________________________
Mutations Level 3 and 4 cover all three mutation types — silent, missense, and nonsense — by actually comparing two sequences and seeing the protein consequences. This connects to AP Biology's treatment of mutations and directly sets up the sickle cell capstone in Level 6.
________________________________________
Gene Regulation & Promoters The motif-finding problems in Level 4 connect to transcription factor binding sites and promoter sequences like the TATA box. Students learn that specific short sequences have enormous biological significance — the basis of all gene regulation.
________________________________________
Biotechnology & Genetic Engineering The restriction enzyme problem in Level 4 is pure biotechnology curriculum — the same concept behind gel electrophoresis labs that most biology classes already run. Students find EcoRI and HindIII cut sites computationally, which mirrors exactly what researchers do before designing an experiment.
________________________________________
Heredity & Genetic Variation Hamming distance (Level 4) and the consensus sequence problem give students a quantitative way to think about genetic variation within a population — connecting to Hardy-Weinberg, allele frequencies, and the idea that individuals in a species share most but not all of their DNA.
________________________________________
Epigenetics & Gene Expression The GC sliding window and CpG island problem in Level 5 introduces epigenetics — one of the most exciting modern additions to high school biology. CpG islands near promoters are central to DNA methylation and gene silencing, which connects to cancer biology and development.
________________________________________
Genomics & Bioinformatics Level 6 introduces the tools professional scientists actually use — FASTA format, ORF finding, sequence assembly. This is where students get a genuine glimpse of what genomics research looks like, connecting to discussions of the Human Genome Project and modern personalized medicine.
________________________________________
Evolution & Phylogenetics The distance matrix problem in Level 6 is a direct computational version of cladograms and phylogenetic trees that students draw by hand. Comparing Human, Chimp, Gorilla, and Mouse sequences makes the molecular clock and common ancestry tangible in a way a textbook diagram rarely achieves.
________________________________________
Human Genetics & Disease The sickle cell capstone in Level 6 ties everything together. Students apply every skill they've built — finding a mutation, identifying the changed codon, classifying the mutation type, translating both proteins — to a real disease that affects real people. It connects to Mendelian genetics, codominance, natural selection in malaria regions, and the ethics of genetic screening.

