# -*- coding: utf-8 -*-

# This programa make a graph of approximation error vs n-step

# library for graph
from matplotlib import pyplot as plt

import math

import numpy as np 

#Constantes
#size of interval
b = 0.1
r = 1
c = 0.4

#Variables

A = []
B = [c]
R = []
xe =[]
xe1 = []
xe2 = []
xe3 = []
# equation definition

def xr(vari, r):
   xr1 = r * vari * (1.0 - vari)
   return xr1


for i in range(100):
   a = b * i
   #A.append(a)
   R.append(a)

L=0

for j in range(100):
   B = [0.7]
   #while i < 5:
   for i in range(100):
      c = xr(B[i],R[j])
      B.append(c)
      print(" ", i)
      #print (" ",B[i])
      #i=i+1
      if i ==20:
         xe.append(B[i])
      elif i==21:
         xe1.append(B[i])
      elif i==22:
         xe2.append(B[i])
      elif i==23:
         xe3.append(B[i])         
      L=L+1

print(" ",len(xe), "--","", B[50], "", L)


A=[]
for i in range(100):
   A.append(xe[i])
   

#plt.plot(R,A)
plt.scatter(R,A, marker= '*', color='red')
#plt.plot(R,xe1, marker='*')
plt.scatter(R,xe1)
plt.scatter(R,xe2)
plt.scatter(R,xe3)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("r (s)")
plt.ylabel("Xr de equilibrio")
plt.title("test")
plt.show()

#for i in range(100):
#   print(" ",i, "-- ", xe[i])