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
xei = []

k=[]

step = 100
step1 = 1000

# equation definition

def xr(vari, r):
   xr1 = r * vari * (1.0 - vari)
   return xr1


for i in range(step):
   a = b * i
   #A.append(a)
   R.append(a)

for i in range(step1):
    dk= (4-3.5)/step1
    ks= 3.5 + i*dk
    k.append(ks)



for j in range(step1):
    xe_ = [0.5]
    for i in range(step-1):
        x = xr(xe_[i],k[j])
        xe_.append(x)
    xe.append(xe_)




#plt.plot(R,A)
#plt.scatter(k,xe[19], marker= '*', color='red')


for i in range(step1):
    tt = []
    for j in range(step):
        tt.append(k[i])
    plt.scatter(tt,xe[i], marker= '.', color='red')
    #plt.scatter(k,xei[i], marker= '.', color='red')
#plt.plot(R,xe1, marker='*')


plt.title("Variación de la ecuación logística")
plt.xlabel("K")
plt.ylabel("X")
plt.show()