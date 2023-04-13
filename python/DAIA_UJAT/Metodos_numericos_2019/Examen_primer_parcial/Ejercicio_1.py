# -*- coding: utf-8 -*-

# Este es el ejercicio uno del examen de primer parcial 2019

# library for graph
from matplotlib import pyplot as plt

#This example is a exercise of numerical method


#number of points
p = 20
# step
a = 1
# gravity acceleration (m/s^2)
g = 9.8  
# skydiver mass (kg)
m =  70
#coefficient of resistance (kg/s)
c = 15.00 
#coefficient of resistance (kg/s) after 10 s
ca = 55.0 
#initial velocity (m/s)
v0 = -15.00


t = [0]
v = [-15.00]

print ("==========================================")
print ("        t       ##        v (m)           ")
print ("==========================================")

print ("       ",t[0],"           " ,  v[0])


for i in range(p):
    ti = a*(i+1) 
    t.append(ti)
    if t[i] < 15:
        vf = round((g-((c*v0)/m))*a + v0,2)
        v.append(vf)
        print   ("       ",ti ,"           " ,  vf)
        v0=vf
    elif t[i] > 14:
        vf = round((g-((ca*v0)/m))*a + v0,2)
        v.append(vf)
        print   ("       ",ti ,"           " ,  vf)
        v0=vf
    else:
        continue

plt.plot(t,v)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Ejercicio uno")
plt.show()