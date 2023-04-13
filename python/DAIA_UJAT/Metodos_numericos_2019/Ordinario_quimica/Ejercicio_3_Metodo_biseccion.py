# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function

def Volumen(x):
   p = 4*x**(3) -6*x**(2) + 7*x -2.3
   return p


#first interval

a = 0.0000
b = 1.0000

#i = 0
#


print ("=================================================")
print ("            metodo de biseccion                  ")
print ("=================================================")

for i in range(6):
    xr =(a+b)/2    
    if Volumen(a) * Volumen(xr) < 0:
        print (" ",xr)
        b = xr
        #i= i + 1
    elif Volumen(xr) * Volumen(b) < 0:
        print (" ", xr)
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr