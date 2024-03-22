# -*- coding: utf-8 -*-
"""Inferring mRNA from Protein.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y3VvCOhbK6_ULgMOaUx_7KMIDng89g8y

Inferring mRNA from Protein   https://rosalind.info/problems/mrna/
"""

from google.colab import drive
drive.mount('/content/drive')

#data=open('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Sample_Dataset/Inferring_mRNA_from_Protein.txt') #small test data
data=open('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Dataset/rosalind_mrna.txt')  #data for submission
data=data.read().strip()
data

codontab = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

from collections import defaultdict

aminotab = defaultdict(list)
for codon, aa in codontab.items():
    aminotab[aa].append(codon)

aminotab

number=[]
for n in range (len(data)):
  number.append(len(aminotab[data[n]]))

number.append(3) #Don't neglect the importance of the stop codon in protein translation.

result=1
for x in number:
  result = result * x

result

result % 1000000