# -*- coding: utf-8 -*-

# This programa make a graph of approximation error vs n-step

# library for graph
from matplotlib import pyplot as plt

import math

import numpy as np 

#A = [[2, 5, 8, 6 ], [6, 4, 9, 7], [2, 4, 7, 9]]

A = [[1, 3, 4, 6, 7, 7], [1, -7, -7, 4, 5, -1], [2, 9, -2, -3, 1, -3], [7, 8, 3, -4, -8, 5], [9, 1, -2, 11, -13, 3]]

AB = [[1, 3, 4, 6, 7], [1, -7, -7, 4, 5], [2, 9, -2, -3, 1], [7, 8, 3, -4, -8], [9, 1, -2, 11, -13]]

#AB = [[2, 5, 8 ], [6, 4, 9], [2, 4, 7]]

print ("La matriz ha resolver es ")
for i in range(len(A)):
    print (" ",A[i])

c = np.linalg.det(AB)
print ("Su determinante ", c )

# Procesos de gauss
def g(A, k):
    AA =[] #= [A[0] ]
    for i in range(len(A)-1):
        aa = [ ]
        B= []
        for j in range(len(A[0])):
            B.append(A[0][j]*(A[i+1][k]/A[0][k]))
            aa.append(A[i+1][j] - B[j])
        AA.append(aa)
    return AA

# Sustitución_atras

# Esto funciona sin la def
#def h(A, g):
#    h =[ ]
#    h.append(A[0])
#    f = g(A, 0)
#    h.append(f[0])
#    AA =[ ]
#    for i in range(len(A)-2):
#        f = g(f, i+1)
#        h.append(f[0])
 #   


def h(A):
    h =[ ]
    h.append(A[0])
    #f = g(A, 0)
   
    for k in range(len(A)-1):
        AA =[] #= [A[0] ]
        print ("valor k", k)
        for i in range(len(A)-(k+1)):
            print ("valor i", i)
            aa = [ ]
            B= []
            for j in range(len(A[0])):
                print ("valor j", j)
                B.append(A[k][j]*(A[i+(k+1)][k]/A[k][k]))
                aa.append(A[i+(k+1)][j] - B[j])
            AA.append(aa)
            A[i+1] = (AA[i])
#        print (" ", A[k+1])
#        A[k+1] = AA[k+1]
        h.append(AA[0])
    return h

s = h(A)

d = len(s)
dd = len(s[0])
x = []
x.append(round(s[d-1][dd-1] / s[d-1][dd-2],0) )
#c = []
bb = []
for i in range(d-1):
    xx=0
    bb.append(s[d-2-i][dd-1])
    for j in range(i+1):
        xx = xx + s[d-2-i][dd-2-j]*x[j]
    a =  bb[i]- xx
    x.append(a/s[d-2-i][d-2-i])





#for i in range(d-2):
#    xx = 0
#    for j in range(dd-3):
#        xx = xx + (s[d-i-2][dd-1] - (s[d-i-2][dd -2-j] * x[i]) )
#        x.append(xx/(s[d-i-2][dd-2-i]))






print ("La matriz A se transformo usando el método de Gauss Simple en la matriz ")

for i in range(len(A)):
    print (" ",s[i])


print ("Los resultado son: ")

for i in range(len(A)):
    print ("x",i+1,"= ", x[d-i-1])



