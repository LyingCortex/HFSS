# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:23:32 2016

@author: LY
"""

import math
import numpy as np
import matplotlib.pyplot  as plt

f=12.5
wl = 300/f


#t1 = 10**(-1/10)
#t2 = 10**(-3/10)

t1 = 10**(-1/20)
t2 = 10**(-3/20)

th1 = math.acos(t1)/math.pi  * 180   # deg
th2 = math.acos(t2)/math.pi * 180    #deg


#w = np.linspace(0.1, 1000, 1000)
#p = np.abs(1/(1+0.1j*w))
#
#plt.subplot(221)
#plt.plot(w, p, lw=2)
#plt.xlabel('x')
#plt.ylabel('y')
#
#plt.subplot(222)
#plt.semilogx(w, p, lw=2)
#plt.ylim(0, 1.5)
#plt.xlabel('log(x)')
#plt.ylabel('y')
#
#plt.subplot(223)
#plt.semilogy(w, p, lw=2)
##plt.ylim(0, 1.5)
#plt.xlabel('x')
#plt.ylabel('log(y)')
#
#plt.subplot(224)
#plt.loglog(w,p,lw=2)
#plt.xlabel('log(x)')
#plt.ylabel('log(y)')
#
#plt.show()


plt.figure(2)
theta = np.arange(0, 2*np.pi, 0.02)
plt.subplot(121, polar= True)
plt.plot(theta, 2*np.ones_like(theta), lw=2)
plt.plot(theta, theta/6, '--' , lw=2)

plt.subplot(122, polar = True)
plt.plot(theta, np.cos(5*theta),'--', lw=2)
#plt.plot(theta, np.sin(5*theta),'--', lw=2)
plt.plot(theta, 2*np.cos(4*theta),lw=2)
plt.rgrids(np.arange(0.4,2,0.4),angle =130)
plt.thetagrids([0,45,90])
plt.show()

plt.figure(3)
theta1 = np.arange(0, 2*np.pi, 0.01)
plt.plot(polar = True)
plt.plot(theta1, np.cos(2*theta1))