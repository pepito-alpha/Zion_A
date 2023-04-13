# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function
def f(x):
    f = 0.0
    f = 2*x*x*x-11.7*x*x+17.7*x-5
    return f
#Definicion de derivated function
def g(x):
    g = 0.0 
    g = 6*x*x - 23.4*x + 17.7
    return g

#initial value
x1 = 3


print "==============================================="
print "             Newton-Rapshon Method             "
print "==============================================="


for i in range(6):
    x = x1 - (f(x1))/(g(x1)) 
    print x
    x1 = x



print "==============================================="
print "             Método de la secante              "
print "==============================================="

x1 = 3
x2 = 4

for i in range(5):
    y = x2 - (f(x2)*(x1-x2))/(f(x1)-f(x2)) 
    print y
    x1 = x2
    x2 = y     



print "====================="
z =f(3.3265)
print z
