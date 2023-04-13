# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#This example is a exercise of numerical method

x1 = [0.0287, 0.057, 0.0858, 0.1046, 0.1452, 0.2173, 0.2787, 0.3579, 0.405, 0.448, 0.5052, 0.5432, 0.6332, 0.6605, 0.6945, 0.7327, 0.7752, 0.7922, 0.908, 0.9448]

y1 = [0.027153543, 0.042809829, 0.052018555, 0.057649256, 0.088665068, 0.108490413, 0.132894131, 0.152409222, 0.161179008, 0.162782094, 0.170651111, 0.161577209, 0.151368561, 0.145342622, 0.138547932, 0.128006095, 0.118759934, 0.113468089, 0.061191066, 0.047517779]

yc = [ ]

dy =[ ]



dy2=0.0

mini = {}

a = [ ]
b = [0 ]

def g(a,b,x,i,j,k):
    g = -x[i] * math.log(x[i]+a[j]*(1-x[i]), math.e) - (1-x[i])* math.log((1-x[i]) + b[k]*x[i], math.e)
    return g

for i in range(9):
    h = round((i+1)/10,4)
    a.append(h)


#print ("  x1     G/RT     g/rt")

#for i in range(20):
#    yc.append(round(g(b,b,x1,i,0,0 ),6))
#    dy.append(round(y1[i] - yc[i],6))
#    dy2 = dy2 + dy[i]**2
#    print ("   ", x1[i], "    " ,y1[i], "    ", yc[i], "  ", dy[i])

#print ("El valor de dy2 es ", dy2)

#dy2 = 0.0 


for k in range(9):
    for j in range(9):
        dy2=0.0
        dy = [ ]
        yc = [ ] 
        for i in range(20):
            yc.append(round(g(a,a,x1,i,j,k),6))
            dy.append(round(y1[i] - yc[i],6))
            dy2 = dy2 + dy[i]**2

        mini[dy2] = [a[j], a[k]]
        #h.append(dy2)
        #hh.append((a[j], a[k]))

p = min(mini)

print ("Este es el valor mas pequeño", p, "los valores de delta_1, delta 2 son ", mini[p] )
    