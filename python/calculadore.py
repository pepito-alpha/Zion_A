# -*- coding: utf-8 -*-



import math as np

def f(x):
    h = x- x*(((np.log(x))**(2))/((x+1)*((np.log(x+1))**(2))))
    return h



def g(x):
    h = x - x*(((np.log(x))/(np.log(x+1)))+((np.log(x))/(x*np.log(x+1))))
    return h


a = np.pow(1,10)
b=1000000000000000000000000000


c= 1e+2
d=100-c

print("valor ",d)

print("Este es el valor ",f(b))