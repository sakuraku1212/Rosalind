# -*- coding: utf-8 -*-
"""Finding a Spliced Motif.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h-Nu8dqeSUGAR6MHjAASFhRoOLoN6B74

Finding a Spliced Motif   https://rosalind.info/problems/sseq/
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
#data=SeqIO.parse('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Sample_Dataset/Finding_a_Spliced_Motif.txt', 'fasta') #small test data
data=SeqIO.parse('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Dataset/rosalind_sseq.txt','fasta') #data for submission
data=list(data)
data

data[0].seq.find(data[1].seq[0])

position=[]
pos=0

for n in range(len(data[1].seq)):
  for m in range (len(data[0].seq)):
    if data[0].seq[m] == data[1].seq[n] and m>pos:
      pos=m
      position.append(m+1)
      break

print(*position, sep=' ')
