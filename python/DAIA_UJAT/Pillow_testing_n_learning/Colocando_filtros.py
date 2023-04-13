#!/usr/bin/python3

#The ImageFilter module contains definitions for a pre-defined set of filters, which can be used with the filter() method. 
#El modulo ImageFilter contiene definiciones de un conjunto de filtros predefinidos, los cuales son usados con el metodo filter().

from PIL import Image, ImageFilter
import sys

try:
    img = Image.open("imagenes/logo_daia_b.png")
    
except IOError:
    print("Unable to load image")    
    sys.exit(1)

blurred = img.filter(ImageFilter.BLUR)

blurred.save("modificado.png")