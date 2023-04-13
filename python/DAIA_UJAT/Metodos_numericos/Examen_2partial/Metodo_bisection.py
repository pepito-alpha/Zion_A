# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function

def Volumen(h):
   p = math.pi * h * h * ((9-h)/3) - 30
   return p

v = Volumen(0.2)

print v


#first interval

a = 0.0000
b = 3.0000

#i = 0
#


print "================================================="
print "            metodo de biseccion                  "
print "================================================="

for i in range(6):
    xr =(a+b)/2    
    if Volumen(a) * Volumen(xr) < 0:
        print xr
        b = xr
        #i= i + 1
    elif Volumen(xr) * Volumen(b) < 0:
        print xr
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr