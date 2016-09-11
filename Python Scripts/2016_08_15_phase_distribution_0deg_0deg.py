# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:30:18 2016

@author: LY
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

D = 149.3
f = D *0.8

x0 = 0
y0 = 0
z0 = 0

xf=0
yf=0
zf= f
pf = (xf, yf, zf)

theta0 = 0/180*np.pi  # deg
phi0 = 0/180*np.pi
f0  = 13.58
lambda0 = 300/f0
k0 = 2*np.pi/lambda0

p0 = (x0, y0, z0)
d0 =  ( (p0[0] -pf[0])**2 + (p0[1] -pf[1])**2 + (p0[2] - pf[2])**2)**0.5

p = 11.5  #mm

p_part = []
p_part.append(p0)
v_part = {}  # point and value


N=13
Points = np.zeros((N,N))

#mp = [[(x0+m*p, y0+ n*p, z0),((x0+m*p-xf)**2 + (y0+ n*p -yf)**2 + (z0 -zf)**2)**0.5]  for m in range(1, 7) for n in range(m+1)]
for m in range(0,7):
    for n in range(m+1):
        p_i = (p0[0]+m*p, p0[1]+n*p, p0[2])
        d_i = ( (p0[0] + m*p-pf[0])**2 + (p0[1]+ n*p -pf[1])**2 + (p0[2] - pf[2])**2)**0.5
        phi_i = k0 * (d_i - np.sin(theta0)*(p_i[0]*np.cos(phi0) + p_i[1]*np.sin(phi0)))
        phi_i_360 =  (phi_i % (2*np.pi))/np.pi*180
        p_part.append(p_i)
        print(m**2 + n**2)
        v_part[m**2 + n **2]= phi_i_360     # it's handable if the dictionary is used
        
for i in range(N):
    for j in range(N):
        Points[i][j] = v_part[(6-i)**2 +(6-j)**2] if ((6-i)**2 + (6-j)**2) in v_part.keys() else 180
        

XX = Points

fig, ax = plt.subplots()
i = ax.imshow(XX, cmap=cm.jet, interpolation='nearest')
fig.colorbar(i)

plt.show()

