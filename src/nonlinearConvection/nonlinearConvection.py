#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt
import time, sys
from math import cos

###
# Also called the burgers equation. can generate discontinuos solutions (a bit like shockwaves) from smooth boundarie conditions
###

### Numerical variables
nx = 601     # number of discrete points
dx = 4.0 / (nx - 1) # cell width (distance between points)
nt = 2000     # number of timesteps
dt = 0.0005  # Zeitschrittweite

print "Gitterweite: ", dx
print "Zeitschrittweite: ", dt

### physical properties
c = 1.0     # wavespeed -> convective speed of the wave

### initial conditions
u = np.ones(nx)     # velocity: square signal u = 2 im intervall 0.5 <= x <= 1
                    # anosnten: u = 1
start = int(0.5 / dx)   # an dieser stelle u = 2
end   = int(1 / dx + 1) # bis hier her

u[ start:end ] = 2

# generates a cosine initial condition
# for i in range(start, end):
#     u[i] = cos(i/10.0) + 0.5 

# plt.plot(u)
# plt.show()

# 
# u(n+x, i) = u(n, i) - u(n, i) * ( dt/dx ) * (u(n, i) - u(n, i-1))

u_temp = np.ones(nx)

for n in range(nt):     #iteriere ueber die Zetschritte nt
    u_temp = u.copy()
    for i in range(1, nx):  # iteriere ueber die Giraumpunkte
        u[i] = u_temp[i] - ( u_temp[i] * (dt/dx) * (u_temp[i] - u_temp[i-1]))     # non-linear
        # u[i] = u_temp[i] - ( c * (dt/dx) * (u_temp[i] - u_temp[i-1]))       # linear

plt.plot(np.linspace(0, 4, nx), u);
plt.show()

