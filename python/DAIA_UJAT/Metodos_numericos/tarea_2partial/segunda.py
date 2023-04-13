# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function
def f(x):
    f = 0.0
    f = -x*x+1.8*x+2.5
    return f
#Definicion de derivated function
def g(x):
    g = 0.0 
    g = -2*x +1.8
    return g

#initial value
x1 = 5


print "==============================================="
print "             Newton-Rapshon Method             "
print "==============================================="


for i in range(6):
    x = x1 - (f(x1))/(g(x1)) 
    print x
    x1 = x



print "==============================================="
print "             Newton-Rapshon Method             "
print "==============================================="

#Definition of function
def ff(x):
    ff = 0.0
    ff = -1+5.5*x-4*x*x+0.5*x*x*x
    return ff
#Definicion de derivated function
def gg(x):
    gg = 0.0 
    gg = 1.5*x*x-8*x+5.5
    return gg

#initial value
xx1 = 4.52


for i in range(20):
    x = xx1 - (ff(xx1))/(gg(xx1)) 
    print x
    xx1 = x

print "==============================================="
print "             b)             "
print "==============================================="

#Definition of function
def df(x):
    df = 0.0
    df = -1+5.5*x-4*x*x+0.5*x*x*x
    return df
#Definicion de derivated function
def dg(x):
    dg = 0.0 
    dg = 1.5*x*x-8*x+5.5
    return dg

#initial value
dx1 = 4.54


for i in range(15):
    x = dx1 - (df(dx1))/(dg(dx1)) 
    print x
    dx1 = x
