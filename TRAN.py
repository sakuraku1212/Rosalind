# -*- coding: utf-8 -*-
"""Transitions and Transversions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1953ZLcgHtJ1JKogciJxMwKwW3HrIXyPT

Transitions and Transversions   https://rosalind.info/problems/tran/

Transversion(Tv): A or G ⇔ C or T

---

Transition (Ts): A ⇔ G, C ⇔ T
"""

try:
    import google.colab
    # Running on Google Colab, so install Biopython first
    !pip install biopython
except ImportError:
    pass

from google.colab import drive
drive.mount('/content/drive')

from Bio import SeqIO
#data=SeqIO.parse('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Sample_Dataset/Transitions_and_Transversions.txt', 'fasta') #small test data
data=SeqIO.parse('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Dataset/rosalind_tran.txt','fasta') #data for submission
data=list(data)
s1=data[0].seq
s2=data[1].seq

s1

s2

"""Transversion(Tv): A or G ⇔ C or T

---

Transition (Ts): A ⇔ G, C ⇔ T
"""

count=0
Tv=0
Ts=0
for n in range (0, len(s1)):
  if s1[n]==s2[n]:
    continue
  elif s1[n]=='G' and s2[n]=='A':
    Ts +=1
  elif s1[n]=='G' and s2[n]=='T':
    Tv +=1
  elif s1[n]=='G' and s2[n]=='C':
    Tv +=1

  elif s1[n]=='C' and s2[n]=='A':
    Tv +=1
  elif s1[n]=='C' and s2[n]=='T':
    Ts +=1
  elif s1[n]=='C' and s2[n]=='G':
    Tv +=1

  elif s1[n]=='A' and s2[n]=='C':
    Tv +=1
  elif s1[n]=='A' and s2[n]=='T':
    Tv +=1
  elif s1[n]=='A' and s2[n]=='G':
    Ts +=1

  elif s1[n]=='T' and s2[n]=='C':
    Ts +=1
  elif s1[n]=='T' and s2[n]=='A':
    Tv +=1
  elif s1[n]=='T' and s2[n]=='G':
    Tv +=1
print(round(Ts/Tv, 11))
