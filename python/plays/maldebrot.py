
import numpy as np


def mandelbrot(a):
    z = 0
    ran= range(1,50,1)
    for i in ran:
        z = z^2 + a
#    end
    return z
#end

ra = np.arange(1.0, -1.0, 0.05)
ra2 = np.arange(-2.0, 0.5, 0.0315)


for y in ra: 
    for x in ra2:
        if abs(mandelbrot(complex(x, y))) < 2:  
            print("*")
        else: 
            print(" ")
#    end
    print()
#end