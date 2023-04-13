# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt

#This example is a exercise of numerical method


#number of points
p = 10
# step
a = 0.1
# k constant (dia^-1)
k=0.2  
#initial velocity (Bq/l)
c0 = 10.0


t = [0]
c = [10.0]

print ("==========================================")
print ("        t       ##        c (Bq/l)           ")
print ("==========================================")

print ("       ",t[0],"           " ,  c[0])


for i in range(p):
    ti = a*(i+1)
    ti = round(ti, 1) 
    t.append(ti)
    cf = -k * c0 * a + c0
    cf = round(cf, 4)
    c.append(cf)
    print   ("       ",ti ,"           " ,  cf)
    c0 = cf

plt.plot(t,c)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("tiempo (s)")
plt.ylabel("Concentración (Bq/l)")
plt.title("Ejercicio dos")
plt.show()