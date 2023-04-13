# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#This example is a exercise of numerical method

x1 = [0.0287, 0.057, 0.0858, 0.1046, 0.1452, 0.2173, 0.2787, 0.3579, 0.405, 0.448, 0.5052, 0.5432, 0.6332, 0.6605, 0.6945, 0.7327, 0.7752, 0.7922, 0.908, 0.9448]

y1 = [0.027153543, 0.042809829, 0.052018555, 0.057649256, 0.088665068, 0.108490413, 0.132894131, 0.152409222, 0.161179008, 0.162782094, 0.170651111, 0.161577209, 0.151368561, 0.145342622, 0.138547932, 0.128006095, 0.118759934, 0.113468089, 0.061191066, 0.047517779]

yc = [ ]

dy =[ ]

n = 8

dy2=0.0

mini = {}

a = [ ]
b = [ ]

def g(a,b,x,i,j,k):
#    g = round(-x[i] * math.log(x[i]+a[j]*(1-x[i]), math.e) - (1-x[i])* math.log((1-x[i]) + b[k]*x[i], math.e),10)
    g = round(-x[i] * math.log(x[i]+a[j]*(1-x[i]), 2.71828) - (1-x[i])* math.log((1-x[i]) + b[k]*x[i], 2.71828),10)
    return g


aa = 0.0000000000
bb = 0.0000000000

for l in range(n): 
    a = [ ]
    b = [ ]
    mini = { }
    if l==0:
        for i in range(20):
            h = round(aa + ((i+1)/10),10)
            a.append(h)
#
        for i in range(20):
            h =  round(bb +((i+1)/10),10)
            b.append(h)
#
        for k in range(20):
            for j in range(20):
                dy2=0
                dy = [ ]
                yc = [ ]
                for i in range(20):
                    yc.append(g(a,b,x1,i,j,k))
                    dy.append(round(y1[i] - yc[i],10))
                    dy2 = round(dy2 + dy[i]**2,10)
                    dirFichero = './fichero_uno.txt'
                    fichero = open(dirFichero, 'a+')
                    #for l in yc:
                    fichero.write(str(yc[i]) + '\n')
                    fichero.close()
#
                mini[dy2] = [a[j], b[k]]
#        
        p=min(mini)
        aa = mini[p][0]
        bb = mini[p][1]
    elif l!=0:
        for i in range(10):
            h = round(aa - ((i+1)/(10**(l+1))),10)
            a.append(h)
#
        for i in range(15):
            h = round(aa + ((i)/(10**(l+1))),10)
            a.append(h)
#
        for i in range(10):
            h = round(bb - ((i+1)/(10**(l+1))),10)
            b.append(h)
#
        for i in range(10):
            h = round(bb + ((i)/(10**(l+1))),10)
            b.append(h)
#
        for k in range(20):
            for j in range(20):
                dy2=0
                dy = [ ]
                yc = [ ] 
                for i in range(20):
                    yc.append(round(g(a,b,x1,i,j,k),10))
                    dy.append(round(y1[i] - yc[i],10))
                    dy2 = round(dy2 + dy[i]**2,10)
                mini[dy2] = [a[j], b[k]]        
        p=min(mini)
        aa = mini[p][0]
        bb = mini[p][1]
  

p = min(mini)

plt.plot(x1,y1, 'D',x1,yc, '^')

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("G/RT")
plt.ylabel("x")
plt.title("Ejercicio tres")
plt.show()

dirFichero = './fichero_escribir.txt'
fichero = open(dirFichero, 'w')
for l in yc:
    fichero.write(str(l) + '\n')
fichero.close()

print ("Este es el valor mas pequeño", p, "los valores de delta_1, delta 2 son ", mini[p] )


    