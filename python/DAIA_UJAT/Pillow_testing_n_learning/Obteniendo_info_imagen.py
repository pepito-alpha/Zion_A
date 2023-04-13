#!/usr/bin/python3

#Pillow allows us to get some basic information about the image. 
#Pillow nos permite obtener alguna información basica de la imagen.

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/logo_daia_b.png")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
print("Format: {0}\nSize: {1}\nMode: {2}".format(tatras.format, 
    tatras.size, tatras.mode))