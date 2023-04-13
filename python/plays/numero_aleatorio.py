## -*- coding: utf-8 *-*
#!/usr/bin/env python

import random


def g(a,b,c,d,e,ff):
    ff = ((e + c - b)*(a / d )) * 100 
    return e




print("Que año es:")
#year = float(input())
year = 2022
print(year)

print("Que mes es:")
#mes = float(input())
mes = 6
print(mes)

print("Que estación es:")
#estacion = int(input())
estacion = 2
print(estacion)

print("Que día es luna llenas:")
#luna = int(input())
luna = 14
print(luna)

print("Que día es :")
#dia = int(input())    
dia = 27
print(dia)


print("========================================")
print("========================================")


p = 0.0
p = g(year, mes, luna , estacion, dia, p)

p = round(p,0)
print(p)

p=int(p)
n=p-1
for j in range(p):
    if j != n:
        for i in range(6):
            a = random.randrange(1,56)
    elif j == n:
        for i in range(6):
           a = random.randrange(1,56)
           print( a)