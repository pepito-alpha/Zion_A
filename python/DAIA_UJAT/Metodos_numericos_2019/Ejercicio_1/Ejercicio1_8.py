# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
#import numpy as np
import math

#This example is a exercise of numerical method

#number of points
p = 20
# step
a = 0.5
# transversal area (m^2)
A = 1200.0  
#flow (m^3/d)
Q = 500.0 
#initial velocity (m/s)
y0 = 0.0

t = [0.0]
y = [0.0]

print ("==========================================")
print ("        t       ##        y (t)           ")
print ("==========================================")

print   ("       ",t[0] ,"           " ,  y[0])

for i in range(p):
    ti = a*(i+1) 
    t.append(ti)
#    yf = ((3/A) * Q * ((math.sin(math.radians(ti))))**2) * a - (Q/A)*a + y0
    yf = ((3/A) * Q * ((math.sin(ti)))**2) * a - (Q/A)*a + y0
    y.append(yf)
    print   ("       ",ti ,"           " ,  yf)
    y0 = yf
 
plt.plot(t,y)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("Tiempo (d)")
plt.ylabel("Profundidad (m/s)")
plt.title("Ejercicio ocho")
plt.show()