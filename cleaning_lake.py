import matplotlib.pyplot as plt
import numpy as np
from pylab import *

with open('bif_output.txt', 'w') as bifout:
    
    b = 0.9
    g = 0.03
    s = 0.085
    ze = 13.7520
    h = 0.0006
    e = 0.65
    p = (1.0 / b)*(g + s / ze + h)
    DO = 11.1
    zh = 4.915
    kt = 1.6245
    alpha = 0.12
    dpdt = 0.0
    
    for l in np.arange(0.02,0.51,0.01):
        for x in np.arange(0.0,30.01,0.01):

            dpdtdummy = dpdt
            R = (14.0/150)*(150-(DO*(50+zh))/(3.8*(1.15*(x**(1.33))/(9+1.15*(x**(1.33))))*kt+alpha))

            if R <= 0:
                R = 0

            r = R/ze
            dpdt = l + r + e * g * x - b * x * p - h * p

            if dpdtdummy < 0:
                if dpdt > 0:
                    print(l,x)
                    bifout.write("%.2f %.2f\n" % (l,x))

            if dpdtdummy > 0:
                if dpdt < 0:
                    print(l,x)
                    bifout.write("%.2f %.2f\n" % (l,x))

        print("\n")
        bifout.write("\n")

        dpdtdummy = 0
        dpdt = 0
                    

bifout.close()
                    
X, Y = [], []
with open('bif_output.txt') as val:
    lines = (line.rstrip() for line in val)
    lines = list(line for line in lines if line) # Non-blank lines in a list
    X = [line.split()[0] for line in lines]
    Y = [line.split()[1] for line in lines]

    plt.plot(X,Y,"o")
    plt.xlabel('P Loading')
    plt.ylabel('Chlorophyll Concentration')
    savefig('bif.png', bbox_inches='tight') # Remove white space around the image
    
