import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy.integrate import ode
import numpy as np
import math

# Step 1: Define system, where x[0] = x and x[1] = y
###############################################################################
def sys(t,x):
    return np.array([ x[0]+(x[1])**2, -1*x[1] ])
###############################################################################

# Step 2: Plot vector field
###############################################################################
# Get the frame out
fig = plt.figure(figsize = (8,6))
ax = fig.add_subplot(1,1,1)

##Quiverplot
# Define a grid and compute direction at each point
x = np.linspace(-5,5,21)
y = np.linspace(-5,5,21)

x1 , y1 = np.meshgrid(x,y)                     #create a grid
dx , dy = sys(0,[x1,y1])                       #compute growth rate on the grid
ax.quiver(x1, y1, dx, dy, pivot='mid')

## If you want your vectors to be normalized, do the following:
## 1. Comment out line 27.
## 2. Uncomment lines 32-36
# m = (np.hypot(dx, dy))                       # norm growth rate 
# m[ m == 0] = 1.                              # avoid zero division errors 
# dx /= m                                      # normalize each arrows
# dy /= m
# ax.quiver(x1, y1, dx, dy, m, pivot='mid')


# Step 3: Solution curves
################################################################################
t0 = 0; tEnd = 5; dt = 0.01;
r = ode(sys).set_integrator('vode', method='bdf',max_step=dt)

## Set as many initial conditions as needed
# Use the loop below to plot a range of initial points
# If only a few points are desired, disable the section below and enable line
# 48, changing the points as needed:
# ic = [[0,1],[1,3]]
#///////////////////////////////
point = [-6, -5]
s = [[point[0],point[1]]]; step = 0.1
a = np.arange(-5,5,step)
for j in range(len(a)):
    new=[];
    while len(s)<=len(a):
        point[1] = point[1]+step
        new = [point[0],point[1]]
        s.append(new)

ic = s
#//////////////////////////////
for k in range(len(ic)):
    Y = [];T = [];S = [];
    r.set_initial_value(ic[k], t0).set_f_params()
    while r.successful() and r.t +dt < tEnd:
        r.integrate(r.t+dt)
        Y.append(r.y)

    S = np.array(np.real(Y))
    ax.plot(S[:,0],S[:,1],color = 'k', lw = 1.25)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)

## Graph labels ##
ax.grid()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Phase space")
fig.show()
input()
