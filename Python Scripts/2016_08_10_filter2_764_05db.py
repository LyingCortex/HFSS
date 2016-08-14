# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:00:37 2016

@author: levi
"""




import math

print('====================================')
print('       ')


f1 = 23.5
f2 = 24.5

fs1 = 23
fs2 = 25

f0 = (f1 + f2)/2
print('f0 = ' + str(f0) + ' GHz')

W = (f2 -f1)/ f0
print('W = ' + str(W))

Omega_s1 = 2/W *(fs1/f0 -1)
Omega_s2 = 2/W *(fs2/f0  -1)
print('Omega_s1 = ' + str(Omega_s1))
print('Omega_s2 = ' + str(Omega_s2))

g = [1, 1.5963, 1.0967, 1.5963, 1]
Qbp = 200
delta_Lp = 4.34/W/Qbp*sum(g[1:-1])
print('delta_Lp = ' + str(delta_Lp) + ' dB')

J01 = J34 = (math.pi * W / 2/g[0]/g[1])**0.5
print('J01/Y0 = J34/Y0 = ' +str(J01))

J12 = J23 = math.pi * W / 2/ (g[1]*g[2])**0.5
print('J12/Y0 = J23/Y0 = ' +str(J12))

Z0 = 74.6865  #ohm

Z0e_01 = Z0e_34 = Z0 *(1+J01+J01**2)
Z0o_01 = Z0o_34 = Z0 *(1-J01+J01**2)
Z0e_12 = Z0e_23 = Z0 *(1+J12+J12**2)
Z0o_12 = Z0o_23 = Z0 *(1-J12+J12**2)
print('Z0e_01 = Z0e_34 = ' + str(Z0e_01))
print('Z0o_01 = Z0o_34 = ' + str(Z0o_01))
print('Z0e_12 = Z0e_23 = ' + str(Z0e_12))
print('Z0o_12 = Z0o_23 = ' + str(Z0o_12))




print('       ')
print('====================================')
