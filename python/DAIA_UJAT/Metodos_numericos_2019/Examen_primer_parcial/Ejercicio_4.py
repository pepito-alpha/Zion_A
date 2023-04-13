# -*- coding: utf-8 -*-

# Este es el ejercicio cuatro del examen de primer parcial 2019
# En este ejercicio hay que calcular la constante c para tener 
# una velocidad de 30 m/s en un tiempo de 10 s.

# library for graph
from matplotlib import pyplot as plt
import math

#This example is a exercise of numerical method

#definiendo la funcion a la que calcualremos la raiz
def f(x, t):
# gravity acceleration (m/s^2)
    g = 9.8  
# skydiver mass (kg)
    m =  70
#Velocidad final (m/s)
    vec = 30
    f = round(((g*m)/x)*(1- math.exp(-(x/m)*t))-vec,4)
    return f


# gravity acceleration (m/s^2)
g = 9.8  
# skydiver mass (kg)
m =  70
#initial velocity (m/s)
v0 = 0
#Velocidad final (m/s)
vec = 30


#number of points
p = 50
# step
step = 0.5

#first interval
a = 21.0000
b = 22.0000


c = [0.5]
v = [v0]

print ("==========================================")
print ("        c       ##        v (m)           ")
print ("==========================================")

print ("       ",c[0],"           " ,  v[0])


for i in range(p):
    ci = step *(i+1) 
    c.append(ci)
    vf = round(((g*m)/ci)*(1-math.exp(-(ci/m)*(10)))-vec,2)
    v.append(vf)
    print   ("       ",ci ,"           " ,  vf)
    v0=vf
    




print ("=================================================")
print ("            metodo de biseccion                  ")
print ("=================================================")

print ("\n\n =================================================")
print ("ciclo    c")

for i in range(8):
    xr =(a+b)/2    
    if f(a,10) * f(xr,10) < 0:
        print (" ",i," ",xr)
        b = xr
        #i= i + 1
    elif f(xr, 10) * f(b,10) < 0:
        print (" ",i," ",xr)
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr




plt.plot(c,v)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("Coeficiente de arrastre (kg/s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Ejercicio cuatro del examen ordinario")
plt.show()