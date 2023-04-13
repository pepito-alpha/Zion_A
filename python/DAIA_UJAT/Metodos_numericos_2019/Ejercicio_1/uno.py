#-*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function
def euler(f, a, v):
    s = f*a + v
    return s 

#This example is a exercise of numerical method

#number of points
p = 20
# step
a = 1

#initial velocity (m/s)
v0 = 0
vi=v0


def f(vi):
# gravity acceleration (m/s^2)
    g = 9.81  
# skydiver mass (kg)
    m =  80
#coefficient of resistance (kg/s)
    c = 10 
#Function definition
    f = (g-(c/m)*vi)
    return f

#Inicialited arrays
t = [0]
v = [0]


print ("==========================================")
print ("        t       ##        v (m)           ")
print ("==========================================")

print ("       ",t[0],"           " ,  v[0])

for i in range(p):
    ti = a*(i+1) 
    t.append(ti)
    vf = euler(f(vi), a, vi)
    #vf = (g-((c*v0)/m))*a + v0
    v.append(vf)
    print   ("       ",ti ,"           " ,  vf)
    vi=vf

plt.plot(t,v)

texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Ejercicio uno")
plt.show()