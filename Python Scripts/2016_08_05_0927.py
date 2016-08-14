# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 09:26:51 2016

@author: levi
"""

import math

o1 = -8.16
o3 = -4.56
o5 = -4.26
o7 = -7.8

o2 = -6.96
o4 = -3.98
o6 = -5.23
o8 = -9.5

o18 = o1 - o8
o27 = o2 - o7
o36 = o3 - o6
o45 = o4 - o5
 
print('=================================')
print('o1-o8 = ' + str(o18))
print('o2-o7 = ' + str(o27))
print('o3-o6 = ' + str(o36))
print('o4-o5 = ' + str(o45))
print('=================================')


o51 = o5 -o1
o48 = o4 -o8

o37 = o3 - o7
o62 = o6 - o2


d_r = 11.634 - 0.82
r1 = 10**(d_r/10)

Z0 = 76.4
Z1 = Z0 * r1


Z1_0 = Z1 * Z0 /(Z1 + Z0)
Z10 = (Z1_0 * Z0) ** 0.5



print('Z1 = ' + str(Z1))
print('Z10 = ' + str(Z10))

print('Z1//Z0 = ' + str(Z1_0))
Z20 = 95.05
print('Z20 = ' + str(Z20))
Z2 = Z20**2 / Z1
print('Z2 = ' + str(Z2))

Z30 =50
print('Z30 = ' + str(Z30))
Z3 = Z30**2 / Z2
print('Z3 = ' + str(Z3))
Z40 =95
Z4 = Z40**2/Z3
Z50 = (Z4*Z0)**0.5

print('Z40 = ' + str(Z40))
print('Z4 = ' + str(Z4))
print('Z50 = ' + str(Z50))