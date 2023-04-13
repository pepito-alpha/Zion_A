# -*- coding: utf-8 *-*
#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy as np

#Estes programa calcula el área de una función en particular
#con aproximación de rectangulos, dividiendo la base en n parte iguales
# n es un variable


#definicion de funcion cuadratica
def f(x):
    g = x*x*x
    return g

#definiendo el intervalo [a, b] 
a = 0
b = 3

# numero de rectangulo
n = 1000

#iniciando calculos

# l es el tamaño de la base
l = (b-a)/n
s = 0.0
c = 0

S = 0.0
C = 0


for i in range(n-1):
    s += f((i+1)*l) * l
    c += 1 

for i in range(n):
    S += f((i+1)*l) * l
    C += 1 

print("el área es a= ",s, "con numero de rectangulos = " ,c ) 

print("el área es a= ",S, "con numero de rectangulos = " ,C ) 

#######################################
#vamos a grafica la evolición de las areas con respecto a n iniciando con n=1
#======================================

nn = 90
#ll = (b-a) / nn

x = []
y = []

x1 = []
y1 = []


for i in range(nn):
    i=i+1
    ll = (b-a) / i
    c=0
    s=0
    for j in range(i):
        if j !=0:
            print ("", ll)
            s += f(j*ll) * ll
            c += 1 
        else:
            continue    
    x.append(c)
    y.append(s)


for i in range(nn):
    i=i+1
    ll = (b-a) / i
    C=0
    S=0
    for j in range(i):
        print ("", ll)
        S += f(b-(j)*ll) * ll
        C += 1 
    x1.append(C)
    y1.append(S)


y2=[]
for i in range(nn):
    y2.append(81/4) 


plt.plot(x,y, 'D',x1,y1, '^', x1,y2, 'b-')

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("Numero de rectangulos")
plt.ylabel("area")
plt.title("Exhaución")
plt.show()