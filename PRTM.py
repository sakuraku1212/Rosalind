# -*- coding: utf-8 -*-
"""Calculating_Protein_Mass.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bEhMgWauPyaqq3FwD2Yv8wDdTMQESPMM

https://rosalind.info/problems/prtm/
"""

from google.colab import drive
drive.mount('/content/drive')

#protein=open('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Sample_Dataset/Calculating_Protein_Mass.txt','r') #small test data
protein=open('/content/drive/MyDrive/Colab_Notebooks/Rosalind/Dataset/rosalind_prtm.txt','r') #data for submission
protein=protein.read()
protein

mass_table={'A':71.03711,
            'C':103.00919,
            'D':115.02694,
            'E':129.04259,
            'F':147.06841,
            'G':57.02146,
            'H':137.05891,
            'I':113.08406,
            'K':128.09496,
            'L':113.08406,
            'M':131.04049,
            'N':114.04293,
            'P':97.05276,
            'Q':128.05858,
            'R':156.10111,
            'S':87.03203,
            'T':101.04768,
            'V':99.06841,
            'W':186.07931,
            'Y':163.06333}

mass_table.keys()
mass_table['A']

mass=0
for n in range (0, len(protein)):
  if protein[n] in mass_table.keys():
    mass=mass+mass_table[protein[n]]

print(mass)
