#Rotating image with Pillow

#The Image.rotate() returns a rotated copy of the image.
#rotate_image.py
# Image.rotate() regresa una copia de la imagen rotada.
#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/logo_daia_b.png")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
rotated = tatras.rotate(-2)
rotated.save('ratado.jpg') 
