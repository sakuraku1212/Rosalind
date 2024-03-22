# -*- coding: utf-8 -*-
"""Enumerating k-mers Lexicographically.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-ryIeTrICnd0ozvBy1VH7Bs0ACZqp5d

Enumerating k-mers Lexicographically   https://rosalind.info/problems/lexf/
"""

import itertools

lst='ABCD'
N=4

def product(lst, N):
  C=[]
  for n in range(N):
    C.append(lst)

    # Unpack operation performed
    # by '*' operator and returning
    # the list containing cartesian
    # product
  return [x for x in itertools.product(*C)]

# list of lists being passed in the method
a=product(lst, N)

for m in range(len(a)):
  print(''.join(a[m]))