## -*- coding: utf-8 *-*
#!/usr/bin/env python

# Este programa suma cualquier expresion matematica

Alfabeto = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "Ñ", "ñ", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]

numero = [1,2,3,4,5,6,7,8,9,0]
numero_string = ["1","2","3","4","5","6","7","8","9","0"]


#=========================================================
# Funcion conta_term
# s define la cantidad de terminos a sumar
# l las posiciones finales de cada termino en la cadena
# r es unb arreglo que tiene un numero y un arreglo r = [s, l]
def conta_term(a):
    A = str(a)
    i = len(A)
    r = []
    s = 1
    l = [0]
    for k in range(i):
        if A[k] == "+":
            s += 1
            l.append(k)
    r.append(s)
    r.append(l)
    return r

#=========================================================

def orde_term(a):
    coeficiente_string = ""
    r = conta_term(a)
    A = str(a)
    i = len(A) 
    for j in range(i):
        for k in numero_string:
            if A[i] == k:
                coeficiente_string += A[i]
            else:
                coeficiente_string = "1"

    
    
    
    #for k in range(i):
    #    if A[k] !=



g = "2c + 34s + 4"

print(" ", conta_term(g))#[0])

#def suma(a):


