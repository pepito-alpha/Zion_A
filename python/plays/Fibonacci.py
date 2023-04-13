# -*- coding: utf-8 *-*
#!/usr/bin/env python

# library for graph
from matplotlib import pyplot as plt


# Fibo calcula la secuencia de fibonacci
def Fibo(b):
    a = [0, 1]
    f = []
    if b==1:
        f.append(a[0])
        return f
    elif b==2:
        f = a
        return f
    elif b>2:
        c=b-2
        for i in range(c):
            d = a[i] + a[i+1]
            a.append(d)
        return a

# Es el numero de iteraciones en la serie de fibonacci        
h=input("¿cuantos terminos fibonacci deseas?\n")
h = int(h)
#h=15

t=range(h)
d = Fibo(h)

#print(" ",len(d))
# imprime en pantalla los valores de la secuencia fibonacci
for i in range(h):
    print(" ",d[i])




# Grafica la secuencia Fibonacci vs el numero de iteraciones
plt.plot(t,d)

#texto1 = plt.text(0, 53, r'Velocidad Terminal', fontsize=10)
plt.xlabel("iteration (d)")
plt.ylabel("Fibonacci number")
plt.title("Fibonacci sequence")
plt.show()