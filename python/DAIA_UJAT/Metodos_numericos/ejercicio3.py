# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt


#This example is a exercise of numerical method

#number of points
p = 11
# step
a = 2
# gravity acceleration (m/s^2)
g = 9.81  
# skydiver mass (kg)
m =  68.1
#coefficient of resistance (kg/m)
c = 0.225 
#initial velocity (m/s)
v0 = 0.0

t = [0]
v = [0]



print "=========================================="
print "        t       ##        v (m)           "
print "=========================================="

print   "       ",t[0] ,"           " ,  v[0]

for i in range(p):
    #print   "       ",v[i] ,"           " ,  vf
    ti = a*i + 2 
    t.append(ti)
    vf = (g-((c * (v0*v0) )/m))*a + v0
    v.append(vf)
    print   "       ",ti ,"           " ,  vf
    v0=vf

plt.plot(t,v)

texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Ejercicio uno")
plt.show()