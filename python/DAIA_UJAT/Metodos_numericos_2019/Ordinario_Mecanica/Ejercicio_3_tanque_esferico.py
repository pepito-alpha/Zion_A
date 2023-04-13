# -*- coding: utf-8 -*-

# library for graph
from matplotlib import pyplot as plt
import math

#Definition of function
def f(h):
   f=0.0
   f = math.pi * h * h * ((9-h)/3) - 30
   return f

#Definicion de derivated function
def g(x):
    g = 0.0 
    g = 6 * math.pi * x - math.pi * x * x
    return g


#initial value
x1 = 3


print ("===============================================")
print ("             Newton-Rapshon Method             ")
print ("===============================================")


for i in range(6):
    x = x1 - (f(x1))/(g(x1)) 
    print (" ", x)
    x1 = x
