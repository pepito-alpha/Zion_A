# -*- coding: utf-8 -*-

# Este es el ejercicio tres del examen de primer parcial 2019

# library for graph
from matplotlib import pyplot as plt
import numpy as np
import math

#definiendo la función de grados de libertad y numero cifras
def es(n):
    es =  0.5 * pow(10, (2-n) )
    return es


#This example is a exercise of numerical method

#Valor verdadero
ev = 4.48168907
#numero al que hay que evaluar en e^x
x = 1.5
# grados de libertad
gl = 4
#inicializando el error
erc = 10.0
#inicializando variable deapoyo
ecc=0
#Minimo error para tener cuatro grados de libertad
min_e = es(gl)

print ("==============================================================")
print ("==============================================================")
print ("Con cuatro grados de libertad el error minimo es ", min_e)
print ("==============================================================")

print ("==============================================================")
print (" Numero de ciclos # e^x  # error verdadero  #   error calculado")
print ("==============================================================")

for i in range(20):
    if erc > min_e:
        ec = round((pow(x, i)) / math.factorial(i) + ecc,7)
        ecc = ec
        j=i+1
        if i==0:
            erv = round(((ev-ecc)/ev)*(100),6)
            print ("        ",j," #      ",ecc," #     ",erv, "# none"  )
            ecca = ecc
        elif i!=0:
            erc = round(((ecc-ecca)/ecc)*100 ,6)
            erv = round(((ev-ecc)/ev)*(100),6)
            print ("        ",j," #      ",ecc," #     ",erv, "#   ", erc  )
            ecca = ecc
    else:
        break
        
