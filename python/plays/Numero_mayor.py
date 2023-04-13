## -*- coding: utf-8 *-*
#!/usr/bin/env python

# Este programa te pide dos numero y de dice quien es el mayor

print("\n\n=======================================================")
print("Programa para identifica el numero mayor de dos numeros")
print("=======================================================")

a = input("Escribe el primer número \n")
b = input("Escribe el segundo número \n")
a = float(a)
b = float(b)

if a==b:
    print("Los numeros ", a, " y ", b, "son iguales") 
elif a>b:
    c = a-b
    print("el número ", a, " es mayor que el numero ", b)
    print("Y su diferencia es ", c)
elif a<b:
    c = b -a
    print("el número ", b, " es mayor que el numero ", a)
    print("Y su diferencia es ", c)

print("=======================================================")
print("hasta pronto")
print("=======================================================\n")
