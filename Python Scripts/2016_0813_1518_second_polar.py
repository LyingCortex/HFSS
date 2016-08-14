# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:18:04 2016

@author: LY
"""


import math
import numpy as np
import matplotlib.pyplot  as plt

import os, re




########



er = 2.5
gammar = (1-er**0.5)/(1+er**0.5)
beta_Ld = [0, 45, 90, 135, 180]
f = 13.58

lambda0 = 300/f

N = len(beta_Ld)
theta = np.arange(0, 2*np.pi, 0.02)
plt.polar(theta, np.ones_like(theta), lw=2)

plt.figure(1)     #  利用 np.angle  和 np.abs 函数进行计算
for i in range(N):
    S12 = S21 = (1-gammar**2)*np.exp(-1j*beta_Ld[i])/(1 - gammar **2 *np.exp(-1j*2*beta_Ld[i]))
    S11 = S22 = gammar*(1-np.exp(-1j*2*beta_Ld[i]))/(1 - gammar **2 *np.exp(-1j*2*beta_Ld[i]))
    mag_S21_c =np.abs( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) )))
    plt.polar(np.angle( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) ))),np.abs( np.cos(theta)*np.exp(1j*theta)*S12 / (1-S11 *np.sin(theta)*np.exp(1j*(theta + np.pi/2) ))))


plt.rgrids(np.arange(0.2,1,0.2),angle =130)
plt.thetagrids(np.linspace(0,330, 12))


plt.show()


###########################



