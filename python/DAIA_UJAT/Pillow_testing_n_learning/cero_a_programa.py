from PIL import Image, ImageFilter

#apertura de la imagen original
foto = Image.open('imagenes/logo_daia_b.png')

#si la imagen no esta en escala de grises, se convierte
if foto.mode != 'L':
    foto = foto.convert('L')

#set de coeficientes originales definidos anteriormente
#coeficientes para el sentido horizontal en formato 3x3
coeficientes_h=[0, 0, 0, -1, 0, 1, 0, 0, 0]

#coeficientes para el sentido vertical en formato 3x3
coeficientes_v=[0, -1, 0, 0, 0, 0, 0, 1, 0]

#factor de division
factor = 2

tamaño = (3,3)
#derivadas parciales, horizontal y vertical
datos_h = foto.filter(ImageFilter.Kernel(tamaño, coeficientes_h, factor)).getdata()
datos_v = foto.filter(ImageFilter.Kernel(tamaño, coeficientes_v, factor)).getdata()
 
datos_derivada = []
 
for x in range(len(datos_h)):
 
    #raiz cuadrada de la suma de los cuadrados
    datos_derivada.append(round(((datos_h[x] ** 2) + (datos_v[x] ** 2)) ** 0.5))
 
 
#set de coeficientes con signo contrario a los originales
#y resto del proceso identico al anterior
coeficientes_h=[0, 0, 0, 1, 0, -1, 0, 0, 0]
coeficientes_v=[0, 1, 0, 0, 0, 0, 0, -1, 0]
 
datos_h = foto.filter(ImageFilter.Kernel(tamaño, coeficientes_h, factor)).getdata()
datos_v = foto.filter(ImageFilter.Kernel(tamaño, coeficientes_v, factor)).getdata()
 
datos_derivada1 = []
 
 
for x in range(len(datos_h)):
 
    datos_derivada1.append(round(((datos_h[x]**2)+(datos_v[x]**2))**0.5))
 
 
datos_bordes = []
 
 
for x in range(len(datos_derivada)):
    
    #suma de los datos de las dos imagenes para conformar la imagen final
    datos_bordes.append(datos_derivada[x] + datos_derivada1[x])
 
 
nueva_imagen = Image.new('L', foto.size)
nueva_imagen.putdata(datos_bordes)

#guardar el resultado
nueva_imagen.save("borrar.png")

#cerrar los objetos de la clase Image
foto.close()
nueva_imagen.close()