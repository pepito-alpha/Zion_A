# -*- coding: utf-8 -*-

#!/usr/bin/python3

from PIL import Image, ImageFilter
 
tamaño = (5,5)
 
coeficientes = [0, 0, -1, 0, 0, 0, -1, -2, -1, 0, -1, -2,  16, -2, -1, 0, -1, -2, -1, 0, 0, 0, -1, 0, 0]
 
factor = 1
 
imagen_original = Image.open("imagenes/logo_daia_b.png")
 
imagen_procesada = imagen_original.filter(ImageFilter.Kernel(tamaño, coeficientes, factor))
 
#se graba el resultado
 
imagen_procesada.save('borrar.png')
 
#se cierran ambos objetos creados de la clase Image
 
imagen_original.close()
 
imagen_procesada.close()