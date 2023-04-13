# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt


#This example is a exercise of numerical method

#number of points
p = 20
# step
a = 1
# gravity acceleration (m/s^2)
g = 9.81  
# skydiver mass (kg)
m =  50
#coefficient of resistance (kg/s)
c = 10
c2 = 50
#initial velocity (m/s)
v0 = 20.0

t = [0]
v = [20]

print "=========================================="
print "        t       ##        v (m)           "
print "=========================================="

print   "       ",t[0] ,"           " ,  v[0]


for i in range(p):
    ti = a*(i+1)
    if ti < 11: 
        t.append(ti)
        vf = (g-((c * v0)/m))*a + v0
        v.append(vf)
        print   "       ",ti ,"           " ,  vf
        v0=vf
    elif ti > 10:
        t.append(ti)
        vf = (g-((c2 * v0)/m))*a + v0
        v.append(vf)
        print   "       ",ti ,"           " ,  vf
        v0=vf
    else:
        continue

plt.plot(t,v)

texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Ejercicio cuatro")
plt.show()