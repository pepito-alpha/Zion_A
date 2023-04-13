#Cropping image with Pillow

#The Image.crop() crops the image.
#crop_image.py
#Recortando imagenes 
#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/logo_daia_b.png")

except IOError:
    print("Unable to load image")
    sys.exit(1)
    
cropped = tatras.crop((100, 100, 350, 350))
cropped.save('borrar.jpg')
