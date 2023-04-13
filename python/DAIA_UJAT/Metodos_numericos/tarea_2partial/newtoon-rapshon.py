# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function
def f(x):
    f = 0.0
    f = 2* math.sin(math.sqrt(x))-x
    return f
#Definicion de derivated function
def g(x):
    g = 0.0 
    g =((math.cos(math.sqrt(x))) / math.sqrt(x)) - 1
    return g

#initial value
x1 = 4


print "==============================================="
print "             Newton-Rapshon Method             "
print "==============================================="


for i in range(6):
    x = x1 - (f(x1))/(g(x1)) 
    print x
    x1 = x


#=================================================
#                       2
#=================================================

#Definition of function
def df(x):
    df = 0.0
    df = 2 * x * x * x - 11.7 * x * x + 17.7 * x- 5
    return df
#Definicion de derivated function
def dg(x):
    dg = 0.0 
    dg =6*x*x-23.4* x + 17.7
    return dg

#initial value
y1 = 3


print "==============================================="
print "             2             "
print "==============================================="


for i in range(6):
    x = y1 - (df(y1))/(dg(y1)) 
    print x
    y1 = x


#=================================================
#                       3
#=================================================

#Definition of function
def fa(x):
    fa = 0.0
    fa = - x * x + 1.8 * x + 2.5
    return fa
#Definicion de derivated function
def ga(x):
    ga = 0.0 
    ga = - 2 * x + 1.8
    return ga

#initial value
z1 = 5


print "==============================================="
print "             3             "
print "==============================================="


for i in range(6):
    x = z1 - (fa(z1))/(ga(z1)) 
    print x
    z1 = x
