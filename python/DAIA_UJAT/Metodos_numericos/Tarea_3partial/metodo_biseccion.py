# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function

def loge(h):
   p = math.log((h*h*h*h)) - 0.7
   return p

def f(x):
    f = (0.8 - 0.3 *x)/x
    return f



#first interval

a = 0.5000
b = 2.0000

#i = 0
#


print "================================================="
print "            metodo de biseccion                  "
print "================================================="

for i in range(6):
    xr =(a+b)/2    
    if loge(a) * loge(xr) < 0:
        print xr
        b = xr
        #i= i + 1
    elif loge(xr) * loge(b) < 0:
        print xr
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr



print "================================================="
print "            metodo de Falsa posicion             "
print "================================================="

for i in range(6):
    xr =b-(loge(b)*(a-b))/(loge(a)-loge(b))    
    if loge(a) * loge(xr) < 0:
        print xr
        b = xr
        #i= i + 1
    elif loge(xr) * loge(b) < 0:
        print xr
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr



#first interval

a = 1.0000
b = 3.0000

#i = 0
#






print "================================================="
print "                5.7                              "
print "================================================="

for i in range(6):
    xr =(a+b)/2    
    if f(a) * f(xr) < 0:
        print xr
        b = xr
        #i= i + 1
    elif f(xr) * f(b) < 0:
        print xr
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr

print "================================================="
print "            metodo de Falsa posicion             "
print "================================================="

for i in range(6):
    xr =b-(f(b)*(a-b))/(f(a)-f(b))    
    if f(a) * f(xr) < 0:
        print xr
        b = xr
        #i= i + 1
    elif f(xr) * f(b) < 0:
        print xr
        a = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr