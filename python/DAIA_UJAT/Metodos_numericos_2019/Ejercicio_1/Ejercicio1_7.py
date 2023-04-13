# -*- coding: utf-8 -*-

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
m =  50
#coefficient of resistance (kg/s)
c = 10 
#coefficient of resistance (kg/s) after 10 s
ca = 50 
#initial velocity (m/s)
v0 = -20


t = [0]
v = [-20]

print ("==========================================")
print ("        t       ##        v (m)           ")
print ("==========================================")

print ("       ",t[0],"           " ,  v[0])


for i in range(p):
    ti = a*(i+1) 
    t.append(ti)
    if t[i] < 11:
        vf = (g-((c*v0)/m))*a + v0
        v.append(vf)
        print   ("       ",ti ,"           " ,  vf)
        v0=vf
    elif t[i] > 10:
        vf = (g-((ca*v0)/m))*a + v0
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