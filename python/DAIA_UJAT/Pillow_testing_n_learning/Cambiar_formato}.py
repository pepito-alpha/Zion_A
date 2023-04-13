

#With the save() method, we can convert an image to a different format. 
#convert2png.py

#!/usr/bin/python3

from PIL import Image
import sys

try:
    tatras = Image.open("imagenes/ujata.jpg")

except IOError:
    print("Unable to load image")
    sys.exit(1)

tatras.save('imagenes/ujata.png', 'png')  
