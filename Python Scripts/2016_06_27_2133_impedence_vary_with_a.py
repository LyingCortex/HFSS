# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:36:03 2016

@author: LY
"""

import math
import matplotlib.pyplot as plt


b = 2.54
mu_ep = 377
N = 164
a = [0.1 * i for i in range(120, N)]
z = [b/aa * 377/(1-(300/15/2/aa)**2)**0.5/2.2**0.5 for aa in a]

plt.figure(1)
plt.plot(a,z)
plt.grid()
plt.figure(2)
plt.plot(z,a)
plt.grid()



for i in range(len(z)):
    if abs(z[i]-50)<0.5:
        print (z[i], a[i])
aa =15
zz= b/aa * 377/(1-(300/20/2/aa)**2)**0.5/2.2**0.5

#N = math.ceil()
N1 = 20
z_step = 50/N1
z_impedence =[50+z_step*i for i in range(N1)]

#a_y = [ai if abs(zi-ai)< else 0  for ai in a for zi in z_impedence]
#a_y = 
#
#a_yy =[]
#for ax in a_y:
#    if a_y != 0:
#        a_yy.append(ax)
al =[]
for zs in z_impedence:
    for i in range(len(z)):
        if abs(zs -z[i])<0.5:
            al.append(a[i])
print('len(al) = '+ str(len(al)))
print('len(z_impedence) = '+ str(len(z_impedence)))
plt.figure(3)
plt.plot(al)
plt.grid()


y_h = 16.3
y_l = 12
Lx = 10
Lxi = Lx /N1
th =[math.pi/Lx*Lxi*i + math.pi/2 for i in range(N1) ]
the = [(math.sin(math.pi/Lx*Lxi*i + math.pi/2)) for i in range(N1) ]
yy = [(y_h-y_l)/4+6+(y_h-y_l)/4*math.sin(math.pi/Lx*Lxi*i + math.pi/2) for i in range(N1) ]
plt.figure(4)
plt.plot(yy)
plt.grid()
xx = [Lxi * i for i in range(N1)]
pos_c = [(0,yy[i],xx[i]) for i in range(N1)]