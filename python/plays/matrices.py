## -*- coding: utf-8 *-*
#!/usr/bin/env python

import numpy as np

a=[[21,22,73,94,15,1,2,3,4,5]]

aa = [[21], [22],[73],[94],[15], [1], [2],[3],[4],[5]]

bb = [[1.38, 51, 4.8, 115], [1.40, 60, 5.6, 130],[1.42, 69, 5.8, 138],[1.54, 73, 6.5, 148],[1.30, 56, 5.3, 122],[1.55, 75, 7.0, 152],[1.50, 80, 8.1, 160],[1.60, 76, 7.8, 155],[1.41, 58, 5.9, 135],[1.34, 70, 6.1, 140]]
bbb = [[1.38,1.40,1.42,1.54,1.30,1.55,1.50,1.60,1.41,1.34],[51,60,69,73,56,75,80,76,58,70], [4.8, 5.6, 5.8, 6.5, 5.3, 7.0, 8.1, 7.8, 5.9, 6.1],
[115, 130, 138, 148, 122, 152, 160, 155, 135, 140]]


b = np.var(a)

print (a)

print (b)

def creator(n,m):
    B = []
    for i in range(n):
        A = []
        for j in range(m):
            A.append(1)
        B.append(A)
    return B

h = creator(1,10)

#==========================================================
#Extrae la diagonal de una matrix y devuelve la matrix con una diagonal

def extradia (B):
    d = B.shape #Determina la dimensión
    C = np.zeros(d)
    for i in range(d[0]):
        for j in range(d[1]):
            if i==j:
                C[i][j]=1/np.sqrt(B[i][j])
            else:
                continue
    return C


#==========================================================
#Calculan la media de una matriz

def media2(x,n):
    media = (1/n)* np.matmul(creator(1,10),x)
    return media 

def media(x,n):
    media = (1/n)* np.matmul([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]],x)
    return media 

#=========================================================
def var(x,y, n):
    varianza= (1/(n-1))*np.matmul(x, np.matmul((np.identity(n) - (1/(n)) * np.matmul([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]],[[1,1,1,1,1,1,1,1,1,1]]) ), y))
    return varianza

c = var(a,aa, 10)

print (c)


print ("\n\n ==========Media==========================\n\n")

med = media2(bb, 10)

print (med)

print ("\n\n ==========Media==========================\n\n")

med2 = media2(bb, 10)

print (med2)

print ("====================================")
print ("\n\n ==========Covarianza====================\n\n")
S1 = np.cov(bbb)

print (S1)

print ("\n\n ==========Covarianza====================\n\n")

S = var(bbb,bb, 10)

print (S)


#==========================================================
print ("\n\n ==========Valor de Correlacion==========================\n\n")


R = np.matmul(extradia(S),np.matmul(S,extradia(S)))
print (R)


print ("\n\n ==========Varianza Total Traza de S==========================\n\n")

VT = np.trace(S)

print (VT)

print ("\n\n ==========Varianza Generalizada determinante de S==========================\n\n")

VG = np.linalg.det(S)

print (VG)

#print (S.shape)



#print (S)
