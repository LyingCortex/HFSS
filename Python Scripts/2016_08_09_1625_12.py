# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:25:02 2016

@author: levi
"""

import math

Z0 = 76.4
Z01 = 30

Z00 = (Z01*Z0)**0.5

r1 = 10**(12.434/10)
Z1 = Z01 * r1


Z1_0 = Z1 * Z01/(Z1 + Z01)
Z10 = (Z1_0 * Z0) ** 0.5



print('Z1 = ' + str(Z1))
print('Z1//Z0 = ' + str(Z1_0))
print('Z00 = ' + str(Z00))
print('Z10 = ' + str(Z10))


Z20 = 95.05
print('Z20 = ' + str(Z20))
Z2 = Z20**2 / Z1
print('Z2 = ' + str(Z2))

Z30 =45
print('Z30 = ' + str(Z30))
Z3 = Z30**2 / Z2
print('Z3 = ' + str(Z3))
Z40 =(Z0*Z3)**0.5

print('Z40 = ' + str(Z40))
