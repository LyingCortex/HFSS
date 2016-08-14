# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import math

print('====================================')
print('       ')


f1 = 23.5
f2 = 24.5

fs1 = 22
fs2 = 26

f0 = (f1 + f2)/2
print('f0 = ' + str(f0) + ' GHz')

W = (f2 -f1)/ f0
print('W = ' + str(W))

Omega_s1 = 2/W *(fs1/f0 -1)
Omega_s2 = 2/W *(fs2/f0  -1)
print('Omega_s1 = ' + str(Omega_s1))
print('Omega_s2 = ' + str(Omega_s2))

g = [1, 1.0315, 1.1474, 1.0315, 1]
Qbp = 200
delta_Lp = 4.34/W/Qbp*sum(g[1:-1])
print('delta_Lp = ' + str(delta_Lp) + ' dB')

J01 = J34 = (math.pi * W / 2/g[0]/g[1])**0.5
print('J01/Y0 = J34/Y0 = ' +str(J01))

J12 = J23 = math.pi * W / 2/ (g[1]*g[2])**0.5
print('J12/Y0 = J23/Y0 = ' +str(J12))


print('       ')
print('====================================')
