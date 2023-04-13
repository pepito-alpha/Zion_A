# -*- coding: utf-8 -*-

# Este es el ejercicio dos del examen de primer parcial 2019

# library for graph
from matplotlib import pyplot as plt

#This example is a exercise of numerical method


#number of points
p = 10
# step
a = 1
# k constant (min^-1)
k=0.017  
#initial temperature (C)
T0 = 68.0
#Room temperature
Ta = 21.0

t = [0]
T = [68.0]

print ("==========================================")
print ("        t       ##        c (Bq/l)           ")
print ("==========================================")

print ("       ",t[0],"           " ,  T[0])


for i in range(p):
    ti = a*(i+1)
    ti = round(ti, 1) 
    t.append(ti)
    Tf = -k * (T0 - Ta) * a + T0
    Tf = round(Tf,4) 
    T.append(Tf)
    print   ("       ",ti ,"           " ,  Tf)
    T0 = Tf

plt.plot(t,T)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.title("Ejercicio dos")
plt.show()