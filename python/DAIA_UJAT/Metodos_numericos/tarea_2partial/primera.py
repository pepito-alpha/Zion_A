# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function

def f(x):
   f = -0.6 * x * x  + 2.4 * x + 5.5
   return f


#first interval
a = 5.0000
b = 10.0000

#i = 0
#


print "================================================="
print "            metodo de biseccion                  "
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


#Definition of function

def g(x):
   g = 4 * x * x * x  - 6 * x * x + 7 * x - 2.3
   return g



#first interval

aa = 0.0000
bb = 1.0000

#i = 0
#


print "================================================="
print "            metodo de biseccion                  "
print "================================================="

for i in range(6):
    xr =(aa + bb)/2    
    if g(aa) * g(xr) < 0:
        print xr
        bb = xr
        #i= i + 1
    elif g(xr) * g(bb) < 0:
        print xr
        aa = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr




#Definition of function

def h(x):
   h = 44 * x * x * x  - 91 * x * x + 85 * x - 26
   return h



#first interval

da = 0.5000
db = 1.0000

#i = 0
#


print "================================================="
print "            metodo de biseccion                  "
print "================================================="

for i in range(6):
    xr =(da + db)/2    
    if h(da) * h(xr) < 0:
        print xr
        db = xr
        #i= i + 1
    elif h(xr) * h(bb) < 0:
        print xr
        da = xr
        #i= i + 1
    else:
        continue #print "La raiz es ", xr