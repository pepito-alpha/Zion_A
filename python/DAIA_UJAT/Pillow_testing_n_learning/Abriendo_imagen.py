#!/usr/bin/python3

#In the first example we read an image file and show it in an external program. 
#En el primer ejemplo leeremos un archivo imagen y lo muestra en un programa externo. 

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/logo_daia_b.png")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
tatras.show()