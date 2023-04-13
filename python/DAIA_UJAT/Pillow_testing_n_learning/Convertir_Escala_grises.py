#With the Image.convert() method, we can produce a black and white image.
#grayscale.py

#Con el metodo Image.convert(), podemos producir una imagen en blanco y negro.

#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/logo_daia_b.png")
    
except IOError:
    print("Unable to load image")
    sys.exit(1)
    
grayscale = tatras.convert('L')

grayscale.save('logo.png', 'png') 
grayscale.show()
