# -*- coding: utf-8 -*-
"""Mendel's First Law.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/132FeP6NHt4JtRdRfsON0ntJBKSeAZxgW

Mendel's First Law   https://rosalind.info/problems/iprb/
"""

k=23  #AA
m=26  #Aa
n=16  #aa

sum=k+m+n
a = k / sum *1
b = (m / sum)*((((m-1)/(sum-1))*0.75)+((k/(sum-1))*1)+((n/(sum-1))*0.5))
c = (n / sum)*(((k/(sum-1))*1)+((m/(sum-1))*0.5))
print(a+b+c)